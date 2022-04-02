from django import views
from django.urls import path, include
from . import views

urlpatterns = [
    path("users/", views.UserDetails.as_view())
]