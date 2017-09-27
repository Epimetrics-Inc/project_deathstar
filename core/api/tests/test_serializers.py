import pytest

from api.models import Document
from api.serializers import VisualizationPostSerializer


class TestVisualizationPostSerializer(object):
    def test_accept_theme_params(self):
        serializer = VisualizationPostSerializer(data={
            'theme_one': 'mnchn',
            'theme_two': 'geriatric',
        })
        assert serializer.is_valid() is True

    @pytest.mark.django_db
    def test_accept_document_params(self):
        doc1 = Document.objects.create(title='test1')
        doc2 = Document.objects.create(title='test2')
        doc1.save()
        doc2.save()
        serializer = VisualizationPostSerializer(data={
            'document_ls_one': [doc1.title],
            'document_ls_two': [doc2.title]
        })
        assert serializer.is_valid() is True
        assert serializer.validated_data['doc_ls_one_id'] == [doc1.pk]
        assert serializer.validated_data['doc_ls_two_id'] == [doc2.pk]

    @pytest.mark.django_db
    def test_accept_document_ls_params(self):
        doc3 = Document.objects.create(title='test3')
        doc4 = Document.objects.create(title='test4')
        doc5 = Document.objects.create(title='test5')
        doc6 = Document.objects.create(title='test6')
        doc3.save()
        doc4.save()
        doc5.save()
        doc6.save()
        serializer = VisualizationPostSerializer(data={
            'document_ls_one': [doc3.title, doc4.title],
            'document_ls_two': [doc5.title, doc6.title]
        })
        assert serializer.is_valid() is True
        assert serializer.validated_data['doc_ls_one_id'] == [doc3.pk, doc4.pk]
        assert serializer.validated_data['doc_ls_two_id'] == [doc5.pk, doc6.pk]

    def test_no_params_provided(self):
        serializer = VisualizationPostSerializer(data={})
        assert serializer.is_valid() is False
        assert serializer.errors['non_field_errors'] == ['Provided documents or themes are insufficient.']

    def test_one_param_provided(self):
        serializer = VisualizationPostSerializer(data={'document_ls_one': ['sad'], })
        assert serializer.is_valid() is False
        assert serializer.errors['non_field_errors'] == ['Provided documents or themes are insufficient.']

    def test_equal_themes_provided(self):
        serializer = VisualizationPostSerializer(data={'theme_one': 'sad', 'theme_two': 'sad'})
        assert serializer.is_valid() is False
        assert serializer.errors['non_field_errors'] == ['Provided themes should not be the same.']

    def test_themes_provided_not_found(self):
        serializer = VisualizationPostSerializer(data={'theme_one': 'mnchn', 'theme_two': 'sad'})
        assert serializer.is_valid() is False
        assert serializer.errors['non_field_errors'] == ['Provided themes are not found.']

    @pytest.mark.django_db
    def test_documents_lists_provided_have_duplicates(self):
        serializer = VisualizationPostSerializer(data={
            'document_ls_one': ['mnchn', 'sad'],
            'document_ls_two': ['sad']})
        assert serializer.is_valid() is False
        assert serializer.errors['non_field_errors'] == ['Provided documents lists have similar values.']

    @pytest.mark.django_db
    def test_documents_lists_provided_not_found(self):
        serializer = VisualizationPostSerializer(data={
            'document_ls_one': ['mnchn'],
            'document_ls_two': ['sad']})
        assert serializer.is_valid() is False
        assert serializer.errors['non_field_errors'] == ['Documents not found: Document matching query does not exist.']
