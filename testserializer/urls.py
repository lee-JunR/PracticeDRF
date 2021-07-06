# testserializer/urls.py

from django.urls import path, include
from .views import PersonAPI,EmailAPI

urlpatterns = [
    path("Person/", PersonAPI),
    path("Email/", EmailAPI),

]