from django.conf.urls import url
from django.views.decorators.cache import cache_page
from rest_framework.routers import DefaultRouter

from .views import DocumentViewSet, VisualizationViewSet

router = DefaultRouter()
router.register(r'documents', DocumentViewSet, base_name='document')

document_list = DocumentViewSet.as_view({
    'get': 'list',
})

document_detail = DocumentViewSet.as_view({
    'get': 'retrieve',
})

visualization_detail = VisualizationViewSet.as_view({
    'get': 'retrieve'
})

visualization_create = VisualizationViewSet.as_view({
    'post': 'create'
})

urlpatterns = [
    url(r'^documents/$', cache_page(5 * 60)(document_list), name='document-list'),
    url(r'^documents/(?P<pk>[0-9]+)/$', cache_page(5 * 60)(document_detail), name='document-detail'),
    url(r'^visualize/$', visualization_create),
    url(r'^visualize/(?P<task_id>.+)/$', visualization_detail),
]
