from django import views
from django.urls import path, include
from . import views

urlpatterns = [
    path("users/", views.Users.as_view()),
    path("users/<int:pk>", views.UserDetails.as_view()),
    path("requests/", views.Requests.as_view()),
    path("requests/<int:pk>", views.RequestDetails.as_view())
]