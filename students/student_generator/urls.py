from django.urls import path

from . import views

urlpatterns = [
    path("generate-student/", views.student_generator, name="student_generator"),
    path("generate-students/", views.students_generator, name="students_generator"),
    path("", views.index, name="index"),
]
