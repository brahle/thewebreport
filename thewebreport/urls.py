from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'thewebreport.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # URL patterns for the Django REST framework
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
