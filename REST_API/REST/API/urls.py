from multiprocessing import managers
from django import views
from django.urls import path, include
from . import views

urlpatterns = [
    path("users/", views.Users.as_view()),
    path("users/<int:pk>", views.UserDetails.as_view()),
    path("requests/", views.Requests.as_view()),
    path("requests/<int:pk>", views.RequestDetails.as_view()),
    path("schedules/", views.Shifts.as_view()),
    path("departments/", views.Departments.as_view()),
    path("departments/<int:pk>", views.DepartmentDetails.as_view()),
    path("managers/", views.Managers.as_view()),
    path("managers/<int:pk>", views.ManagerDetails.as_view()),
    path("login/<str:pk>", views.Logins.as_view()),
    path("login/<str:un>/<str:pw>", views.LoginDetails.as_view()),
    path("schedules/<int:scheduleId>/<str:date>", views.ShiftDetail.as_view()),
    path("schedules/<int:scheduleId>/<str:startRangeDate>/<str:endRangeDate>", views.ShiftRangeDetails.as_view()),
    path("employee/<int:pk>", views.Employee.as_view()),
    path("employee/", views.Employees.as_view()),
    path("scheduleinfo/", views.Schedules.as_view()),
    path("projects/", views.Projects.as_view()),
    path("projects/<int:pk>", views.ProjectDetails.as_view()),
    path("time/", views.TimeLogs.as_view()),
    path("time/<int:pk>", views.TimeLogDetails.as_view()),
]