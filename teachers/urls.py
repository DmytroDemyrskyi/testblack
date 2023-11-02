from django.urls import path

from . import views

urlpatterns = [
    path("teachers_list/", views.teachers_list, name="teachers_list"),
    path("", views.index, name="index"),
]
