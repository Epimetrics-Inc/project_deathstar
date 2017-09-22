from celery.result import AsyncResult
from rest_framework import viewsets, status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework_extensions.mixins import (
    PaginateByMaxMixin, ReadOnlyCacheResponseAndETAGMixin)

from api.tasks import viz_scattertext
from .models import Document
from .serializers import DocumentListSerializer, DocumentGetSerializer, VisualizationPostSerializer, \
    VisualizationGetSerializer


class DocumentViewSet(ReadOnlyCacheResponseAndETAGMixin,
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


    def get_serializer_class(self):
        if self.request.method == 'GET':
            if self.kwargs.get(self.lookup_field, None) is not None:
                return DocumentGetSerializer
            else:
                return DocumentListSerializer


class VisualizationViewSet(CreateModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    """
    retrieve:
    Returns the URL of the visualization HTML  document, retrieved by result id.

    create:
    Creates a new visualization document and returns the task state and id.
    """

    lookup_field = 'task_id'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return VisualizationGetSerializer

        if self.request.method == 'POST':
            return VisualizationPostSerializer

    def get_object(self):
        """
        Retrieve task object from cache
        :return: Response object with status code
        """

        result = AsyncResult(self.kwargs[self.lookup_field])
        obj = {
            'task_id': result.id,
            'task_status': result.state
        }
        if result.state == 'SUCCESS':
            obj['filename'] = result.get()
        else:
            obj['filename'] = ''

        return obj

    def create(self, request, *args, **kwargs):
        """
        Create a new task that triggers a new visualization document
        :param request:
        :param args:
        :param kwargs:
        :return: Response object with status code
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        ids = []

        if data['type'] == 'document':
            ids.append(data['doc_one_id'])
            ids.append(data['doc_two_id'])

        elif data['type'] == 'theme':
            ids.append(data['theme_one'])
            ids.append(data['theme_two'])

        elif data['type'] == 'document_list':
            ids.append(data['doc_ls_one_id'])
            ids.append(data['doc_ls_two_id'])

        res = viz_scattertext.delay(ids, data['type'])
        output = serializer.validated_data
        output['task_id'] = res.id
        output['ids'] = ids
        return Response(output, status=status.HTTP_202_ACCEPTED)
