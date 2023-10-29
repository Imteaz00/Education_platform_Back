from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .serializers import CourseSerializer
from django.http import HttpResponse, HttpRequest, JsonResponse
from .models import Course
# Create your views here.

@api_view(["POST", "GET"])
def addCourse(request):
    if request.method == "POST":
        title = request.data["title"]
        description = request.data["description"]
        techs = request.data["it"]


        if Course.objects.filter(title=title):
            return Response("cf")
        
        courseinfo = Course.objects.create(title = title, description= description, techs = techs)

        courseinfo.save()

        return Response("cgg")
    return Response("cDo")

@api_view(["POST", "GET"])
def TeacherCourses(request, teacher_id):
    if request.method == "POST":
        user = request.user
        course = Course.objects.get(teacher = user)
        serializer = CourseSerializer(course, many = True)
        return Response(serializer.data)
    return Response("")
    

@api_view(["POST", "GET"])
def deleteCourse(request, teacher_id):
    if request.method == "POST":
        user = request.user
        course_id = request.data("course_id")
        course = Course.objects.get(id = course_id)          
        course.delete()
        return Response("")