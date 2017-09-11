from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from api.models import Document


class DocumentTests(APITestCase):
    def test_get_documents(self):
        """
        Ensure we can get document objects.
        """
        url = reverse('api:document-list')
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK

    def test_get_document(self):
        doc = Document.objects.create(title='test')
        doc.save()

        url = reverse('api:document-detail', args=[doc.pk])
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == 'test'
