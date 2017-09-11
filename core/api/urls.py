from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import DocumentViewSet

router = DefaultRouter()
router.register(r'documents', DocumentViewSet, base_name='document')

urlpatterns = [
    url(r'^', include(router.urls)), ]
