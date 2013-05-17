from django.conf.urls import patterns, include, url
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from complaint import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'andbackend.views.home', name='home'),
    # url(r'^andbackend/', include('andbackend.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    # From rest_framework tutorial
    url(r'^api/category/$', views.CategoryListView.as_view()),
    url(r'^api/complaint/$', views.ComplaintListView.as_view()),
    url(r'^api/complaint/hot/$', views.ComplaintListView.as_view(), kwargs={'sorting': 'hot'}),
    url(r'^api/complaint/new/$', views.ComplaintListView.as_view(), kwargs={'sorting': 'new'}),
    url(r'^api/complaint/(?P<pk>[0-9]+)/$', views.ComplaintDetailView.as_view()),
    url(r'^api/image/(?P<pk>[0-9]+)/$', views.ImageView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

urlpatterns = format_suffix_patterns(urlpatterns)
