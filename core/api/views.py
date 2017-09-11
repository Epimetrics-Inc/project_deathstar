from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework_extensions.mixins import PaginateByMaxMixin

from .models import Document
from .serializers import DocumentListSerializer, DocumentGetSerializer


class DocumentViewSet(PaginateByMaxMixin, ListModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Document.objects.all()
    max_paginate_by = 10

    def get_serializer_class(self):
        if self.action == 'list':
            return DocumentListSerializer
        if self.action == 'retrieve':
            return DocumentGetSerializer
