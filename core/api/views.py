from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_extensions.mixins import (
    PaginateByMaxMixin, ReadOnlyCacheResponseAndETAGMixin, DetailSerializerMixin)

from .models import Document
from .serializers import DocumentListSerializer, DocumentGetSerializer


class DocumentViewSet(DetailSerializerMixin, ReadOnlyCacheResponseAndETAGMixin,
                      PaginateByMaxMixin, viewsets.ReadOnlyModelViewSet):
    """
    list:
    Returns a paginated list of all documents and
    allows for full-text searching of title, date, doctype, docnum, and body.

    retrieve:
    Returns a detailed document retrieved by document id.
    """
    queryset = Document.objects.all()
    max_paginate_by = 5
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'date', 'doctype', 'docnum', 'body', 'sign')
    ordering_fields = ('date', 'title')
    serializer_class = DocumentListSerializer
    serializer_detail_class = DocumentGetSerializer
