import pytest

from api.models import Document


@pytest.mark.django_db
def test_get_document_name():
    doc = Document.objects.create(title='test')
    assert str(doc) == 'test'
