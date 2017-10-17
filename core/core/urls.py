from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Documents API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('api.urls', namespace='api')),
    url(r'^docs/', schema_view),
]

from django.conf import settings

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      url(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
