from django.conf.urls import patterns, include, url

from rest_framework import routers

from django.contrib import admin
admin.autodiscover()

from report.views import UserViewSet, GroupViewSet, ReportViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'reports', ReportViewSet)


urlpatterns = patterns('',
    # URL patterns for the Django admin
    url(r'^admin/', include(admin.site.urls)),
    # URL patterns for the Django REST framework
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
