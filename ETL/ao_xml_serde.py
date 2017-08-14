import os
import re
import copy
from lxml import etree
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import postgresql as psql
from sqlalchemy import Column, Integer, String, DATE


def remove_special_chars(string: str) -> str:
    """
    Replaces special char & with its xml equivalent.
    """
    output = copy.deepcopy(string)
    output = re.sub('&', '&amp;', output)

    return output


def read_file(fn: str) -> str:
    """
    Given a filename string, return the contents in string type.
    """
    data = '<data>'
    with open(fn, 'r') as f:
        data += remove_special_chars(f.read())

    data += '</data>'
    return data


def read_xml(fn: str) -> etree._Element:
    """
    Given an XML filename in string type, parse and return an XML object.
    """
    xml = etree.fromstring(
        read_file(fn))

    return xml


def check_errors(dir: str):
    """
    Check errors and generates and error.txt
    """

    logfn = open('errors.txt', 'w')

    fn = []
    for _, _, fn in os.walk(dir):
        fn = fn

    for file in fn:
        try:
            read_xml(file)

        except Exception as error:
            print("Error in ", file)
            try:
                logfn.write(file)
                logfn.write(": ")
                logfn.write(str(error))
                logfn.write('\n')
            except:
                logfn.close()

    logfn.close()


def extract_data(data: etree._Element) -> dict:
    """
    Converts xml data to dict with text and line numbers
    """
    d = {}
    d['date'] = find_tag(data, 'date')
    d['doctype'] = find_tag(data, 'doctype')
    d['docnum'] = find_tag(data, 'docnum')
    d['subject'] = find_tag(data, 'subject')
    d['sign'] = find_tag(data, 'sign')
    d['signtitle'] = find_tag(data, 'signtitle')
    d['image'] = find_tag(data, 'image', all=True)

    return d


def find_tag(data: etree._Element, tag: str, all=False) -> dict:
    """
    Handles missing attribute errors with default inputs
    """
    d = {}
    tag_search = './/' + tag  # to enable recursive search

    if all is False:
        try:
            tag_node = data.find(tag_search)
            d['text'] = tag_node.text
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


Base = declarative_base()


class Document(Base):
    __tablename__ = 'document'

    id = Column(Integer, primary_key=True)
    date = Column(DATE)
    doctype = Column(String)
    docnum = Column(String)
    subject = Column(String)
    body = Column(String)
    sign = Column(String)
    signtitle = Column(String)
    images = Column(psql.JSONB)
    raw_json = Column(psql.JSONB)

    def __repr__(self):
        return self.docnum


def to_sql(data: dict):
    """
    Converts dict to sql
    """
    engine = create_engine('postgresql://dev:dev@localhost/dev')
