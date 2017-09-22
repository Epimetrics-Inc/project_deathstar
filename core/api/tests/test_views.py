import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIRequestFactory

from api.models import Document
from api.views import DocumentViewSet


class DocumentViewSetTests(APITestCase):
    def test_get_documents(self):
        """
        Ensure we can get document objects.
        """
        url = reverse('api:document-list')

        factory = APIRequestFactory()
        view = DocumentViewSet.as_view({
            'get': 'list'
        })

        request = factory.get(url)

        response = view(request)
        print(response)
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_get_document(self):
        doc = Document.objects.create(title='testy')
        doc.save()

        url = reverse('api:document-detail', args=[doc.pk])
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == 'testy'


    def test_does_not_accept_POST_PUT_DELETE(self):
        url = reverse('api:document-list')

        factory = APIRequestFactory()
        view = DocumentViewSet.as_view({
            'get': 'list'
        })

        request = factory.post(url)
        response = view(request)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        request = factory.put(url)
        response = view(request)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        request = factory.delete(url)
        response = view(request)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

class VisualizationViewSetTests(APITestCase):

    def test_get_visualization(self):
        url = reverse('api:visualization-detail', args=[1])
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.celery(result_backend='redis://')
    def test_accept_theme_visualization_task(self):
        url = reverse('api:visualization-create')
        response = self.client.post(url, format='json', data={
            'theme_one': 'mnchn',
            'theme_two': 'specpop'
        })
        assert response.status_code == status.HTTP_202_ACCEPTED

    @pytest.mark.django_db
    @pytest.mark.celery(result_backend='redis://')
    def test_accept_document_visualization_task(self):

        doc1 = Document.objects.create(title='testtyyy', body='asdfd')
        doc1.save()

        doc2 = Document.objects.create(title='testyyy', body='asdsdfd wird')
        doc2.save()

        url = reverse('api:visualization-create')
        response = self.client.post(url, format='json', data={
            'document_one': doc1.title,
            'document_two': doc2.title
        })
        assert response.status_code == status.HTTP_202_ACCEPTED

    @pytest.mark.django_db
    @pytest.mark.celery(result_backend='redis://')
    def test_accept_document_list_visualization_task(self):
        url = reverse('api:visualization-create')

        doc3 = Document.objects.create(title='test3')
        doc4 = Document.objects.create(title='test4')
        doc5 = Document.objects.create(title='test5')
        doc6 = Document.objects.create(title='test6')
        doc3.save()
        doc4.save()
        doc5.save()
        doc6.save()

        response = self.client.post(url, format='json', data={
            'document_ls_one': [doc3.title, doc4.title],
            'document_ls_two': [doc5.title, doc6.title]
        })

        assert response.status_code == status.HTTP_202_ACCEPTED

