from os import name
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home_page, name='home_page'),
]
