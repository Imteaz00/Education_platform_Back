from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("addcourse", views.addCourse, name = "addcourse"),
    path("<int:teacher_id>/teachercourses", views.TeacherCourses, name = "teachercourses"),
    path("<int:teacher_id>/delelteCourse", views.deleteCourse, name = "deletecourses")

]