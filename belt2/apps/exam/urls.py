from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'), 
    url(r'^new$', views.new),
    url(r'^create$', views.create),  
    url(r'^(?P<id>\d+)/show$', views.show),  
    url(r'^(?P<id>\d+)/joined$', views.joined), 
    url(r'^(?P<id>\d+)/dropped$', views.dropped),
    url(r'^(?P<id>\d+)/edit$', views.edit),      
    url(r'^(?P<id>\d+)/delete$', views.delete),  
]