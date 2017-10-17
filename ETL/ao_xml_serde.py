import os
import re
import datetime
import copy
import codecs
from lxml import etree
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import postgresql as psql
from sqlalchemy import Column, Integer, String, DATE
from sqlalchemy.orm import sessionmaker

# EXTRACT


def remove_special_chars(string: str) -> str:
    """
    Replaces special char & with its xml equivalent.
    """
    output = copy.deepcopy(string)
    output = re.sub('&', '&amp;', output)
    # output = re.sub('<', '&lt;', output)
    # output = re.sub('>', '&gt;', output)
    output = re.sub("”", '&quot;', output)
    output = re.sub("‘", '&apos;', output)
    output = re.sub("'", '&apos;', output)
    output = re.sub('"', '&quot;', output)

    return output


def read_file(fn: str) -> str:
    """
    Given a filename string, return the contents in string type with added data tags.
    """
    data = '<data>'
    with open(fn, 'rb') as f:
        raw = f.read()
        file_data = remove_special_chars(codecs.decode(raw, errors='replace'))
        data += file_data

    data += '</data>'
    return data


def read_xml(fn: str) -> etree._Element:
    """
    Given an XML filename in string type, parse and return an XML object.
    """
    xml = etree.fromstring(
        read_file(fn))

    return xml


def process_xml(dir: str) -> dict:
    """
    Check errors and generates and error.txt
    """

    fn = []
    for _, _, fn in os.walk(dir):
        fn = fn

    data = {}
    final = {}

    logfn = open('errors.txt', 'w')

    for file in fn:
        try:
            d = extract_data(read_xml(file))
            tmp_fn = re.sub('.pdf.*$', '', file)
            formatted_date = format_date(d['date']['text'])
            d['date']['text'] = str(formatted_date)
            data[tmp_fn] = d

        except Exception as error:
            logfn.write(str(file) + ": " + str(error) + "\n")

    final = {i: {k: v.get('text')
                 for k, v in data[i].items()} for i in data.keys()}

    for i in final.keys():
        final[i]['image'] = data[i]['image']
        # inefficient / bad fix for now
        final[i]['images'] = final[i].pop('image')
        final[i]['title'] = i
        final[i]['raw_body'] = data[i]
        if final[i]['body'] == None:
            raise AttributeError('Body error for ' + final[i]['title'])

    logfn.close()

    return final


def check_tags(data: etree._Element) -> bool:
    names = set([
        'date',
        'docnum',
        'doctype',
        'subject',
        'body',
        'image',
        'sign',
        'signtitle',
        'missingtext'
    ])
    elements = data.findall('.//')
    tags = set([i.tag for i in elements])
    diff = tags.difference(names)

    if len(diff) != 0:
        raise AttributeError(
            str(diff) + " are mislabeled / do not follow protocols.")

    return True


def extract_data(data: etree._Element) -> dict:
    """
    Converts xml data to dict with text and line numbers
    """
    d = {}
    check_tags(data)
    d['date'] = find_tag(data, 'date')
    d['doctype'] = find_tag(data, 'doctype')
    d['docnum'] = find_tag(data, 'docnum')
    d['subject'] = find_tag(data, 'subject')
    d['body'] = find_tag(data, 'body')
    d['sign'] = find_tag(data, 'sign')
    d['signtitle'] = find_tag(data, 'signtitle')
    d['image'] = find_tag(data, 'image', all=True)

    return d


def get_text(node):
    result = node.text or ""
    for child in node:
        if child.tail is not None:
            result += child.tail
    return result

def find_tag(data: etree._Element, tag: str, all=False) -> dict:
    """
    Handles missing attribute errors with default inputs
    """
    d = {}
    tag_search = './/' + tag  # to enable recursive search

    if all is False:
        try:
            tag_node = data.find(tag_search)
            d['text'] = get_text(tag_node)
            d['line_num'] = tag_node.sourceline
        except AttributeError:
            d['text'] = None
            d['line_num'] = None
        return d

    else:
        for i, j in enumerate(data.findall(tag_search)):
            d[i] = {
                'text': j.text,
                'line_num': j.sourceline
            }
        return d

# TRANSFORM


def rawstr(s):
    """
    Return the raw string representation (using r'') literals of the string
    *s* if it is available. If any invalid characters are encountered (or a
    string which cannot be represented as a rawstr), the default repr() result
    is returned.
    """
    if any(0 <= ord(ch) < 32 for ch in s):
        return repr(s)

    if (len(s) - len(s.rstrip("\\"))) % 2 == 1:
        return repr(s)

    pattern = "r'{0}'"
    if '"' in s:
        if "'" in s:
            return repr(s)
    elif "'" in s:
        pattern = 'r"{0}"'

    return pattern.format(s)


def format_date(s: str) -> str:

    if s is None or s.isspace() or s.lower() == 'nd':
        s = '01/01/2050'

    formats = [
        '%b %d, %Y',
        '%B %d, %Y',
        '%B %d, %Y',
        '%B %d,, %Y',
        '%B, %d, %Y',
        '%B %d,%Y',
        # 
        '%d/%m/%Y',
        '%d/%m/%y',
        '%m/%d/%Y',
        '%m/%d/%y',
        # '-%m/%d/%Y'
        '%d %B,%Y',
        '%d %B%Y',
        '%B %d %Y',
        ' %b %d, %Y',
        '%b %d, %Y',
        '%d %B. %Y',
        '%d %B, %Y',
        '%b %d,%Y',
        '%b %d %Y',
        '%d %b %Y',
        '%d %B %Y',
        '%B,%Y',
        '%B, %Y',
        # '%d/%-m/%Y'
    ]

    s = s.strip().capitalize()
    tmp = ''
    for f in formats:
        if not isinstance(tmp, pd._libs.tslib.Timestamp):
            tmp = pd.to_datetime(s, errors='ignore', format=f)

    if not isinstance(tmp, pd._libs.tslib.Timestamp):
        raise TypeError('date error: ', rawstr(tmp) + ": " + str(type(tmp)))

    return str(tmp.date())


# LOAD
def insert_db(data: dict):
    """
    Converts dict to sql and inserts to postgres
    """
    Base = declarative_base()


    class Document(Base):
        __tablename__ = 'api_document'

        id = Column(Integer, primary_key=True)
        title = Column(psql.TEXT)
        date = Column(DATE)
        created = Column(DATE, default=datetime.datetime.now)
        modified = Column(DATE, default=datetime.datetime.now)
        doctype = Column(psql.TEXT)
        docnum = Column(psql.TEXT)
        subject = Column(psql.TEXT)
        body = Column(psql.TEXT)
        sign = Column(psql.TEXT)
        signtitle = Column(psql.TEXT)
        images = Column(psql.JSONB)
        raw_body = Column(psql.JSONB)

        def __repr__(self):
            return self.title

    engine = create_engine('postgresql://dev:dev@localhost/dev')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add_all([Document(**data[key]) for key in data.keys()])
    session.commit()
