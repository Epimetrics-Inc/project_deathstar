import pytest

from api.models import Document, Label


@pytest.mark.django_db
def test_get_document_name():
    doc = Document.objects.create(title='test')
    assert str(doc) == 'test'


@pytest.mark.django_db
def test_get_label_name():
    doc = Document.objects.create(title='test')
    label = Label.objects.create(document=doc)
    assert str(label) == "%s \n mnchn: %s \n adolescent: %s \n" \
                         "spec_pop: %s \n geriatric: %s \n" % (doc, 0, 0, 0, 0)
