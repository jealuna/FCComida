"""FCComida URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.inicio),
    url(r'^register/$', 'perfiles.views.register', name='register'),
    url(r'^login/$', 'perfiles.views.user_login', name='login'),
    url(r'^logout/$', 'perfiles.views.user_logout', name='logout'),
    url(r'^recupera-password/$', 'perfiles.views.recupera_pass', name='recupera-password'),
    url(r'^comercio-registro/$', 'comercio.views.registro', name='registro'),
    url(r'^comercio-registrado/$', 'comercio.views.exito', name='exito'),
    url(r'^comercio/(?P<pk>\d+)/$', 'comercio.views.detalles_comercio'),
    url(r'^comentario/$', 'comentarios.views.Comentarios', name='comentario'),
    url(r'^califica/$', 'comentarios.views.Calificaciones', name='califica'),
    url(r'^busqueda/', include('haystack.urls')),
]
