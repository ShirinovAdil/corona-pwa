from django.urls import re_path, include
from . import views


urlpatterns = [
    re_path(r'^$', views.homepage, name="homepage"),
    re_path(r'^countries/$', views.countries, name="countries"),
]