from django.conf.urls import url
from .import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>\d+)/courses/destroy$', views.remove, name='remove'),
    url(r'^(?P<id>\d+)/delete$', views.destroy, name='destroy'),
    url(r'^create$', views.create, name='create')
]