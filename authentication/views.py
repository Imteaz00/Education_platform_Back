from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .serializers import UserinfoSerializer
from django.http import HttpResponse, HttpRequest, JsonResponse


# Create your views here.
@api_view(["GET", "POST"])
def home(request):
    if request.method == "POST":
        if "admin_signup" in request.data and request.data["admin_signin"] == 'True':
            if request.user.is_staff:
                return redirect("/admin")
            else:
                return redirect("admin_pass")
            
        if "signup" in request.data and request.data["signup"] == 'True':
            return redirect("signup")
        
        if "t_signup" in request.data and request.data["t_signup"] == 'True':
            return redirect("t_signup")

        if "signin" in request.data and request.data["signin"] == 'True':
            return redirect("signin")
        
        if "signout" in request.data and request.data["signout"] == 'True':
            return redirect("signout")

    users = User.objects.all()
    serializer = UserinfoSerializer(users, many = True)
    return Response(serializer.data)

@api_view(["GET","POST"])
def signout(request):
    logout(request)
    messages.success(request, 'Logged out')
    return redirect("home")


@api_view(["POST"])
def signin(request):
    if request.method == "POST":
        username = request.data["username"]
        password = request.data["password"]

        userinfo = authenticate(username=username, password= password)

        if userinfo is not None:
            login(request, userinfo)
            return redirect("home")

        else:
            messages.error(request, "Error in Username or Password")
    return Response("hsuijdhuf")


@api_view(["POST"])
def teacher_signup(request):
     if request.method == "POST":
        username = request.data["username"]
        # email = request.data["email"]
        password = request.data["password"]
        password2 = request.data["password2"]

        if User.objects.filter(username=username):
            print(123)
            messages.error(request, "Username exists already")
            return redirect("t_signup")
        
        if password!= password2:
            print(234)
            messages.error(request, "Both password does not match")
            return redirect("t_signup")
        
        userinfo = User.objects.create_user(username, password)

        userinfo.save()
        

        messages.success(request, "Account Created Successfully!")

        return redirect("home")


@api_view(["POST"])
def signup(request):
    if request.method == "POST":
        username = request.data["username"]
        email = request.data["email"]
        password = request.data["password"]
        password2 = request.data["password2"]


        if User.objects.filter(username=username):
            messages.error(request, "Username exists already")
            return redirect("signup")
        
        if password!= password2:
            messages.error(request, "Both password does not match")
        
        userinfo = User.objects.create_user(username, email, password)

        userinfo.save()

        messages.success(request, "Account Created Successfully!")

        return redirect("home")


@api_view(["POST"])
def create_admin(request):
    if request.method == "POST":
        username = request.data["username"]
        # email = request.data["email"]
        password = request.data["password"]
        password2 = request.data["password2"]


        if User.objects.filter(username=username):
            messages.error(request, "Username exists already")
            return redirect("create_admin")
        
        if password!= password2:
            messages.error(request, "Both password does not match")
            return redirect("create_admin")
        
        userinfo = User.objects.create_superuser(username, password)

        userinfo.save()
        
        userinfo = authenticate(username=username, password=password)
        login(request, userinfo)
        messages.success(request, "Account Created Successfully!")
        return redirect("home")
    

@api_view(["PUT"])
def edit_profile(request):

    if request.method == "PUT":
        abc = request.data["abc"]
        request.user.abc = abc
        return redirect("edit_profile")
    return Response("jaidfh")


@api_view(["POST"])
def admin_pass(request):
    if request.method == "POST":
        superpass = request.data["superpass"]
        if superpass == "Hehheboy":
            request.user.is_staff = True
            return redirect("create_admin")
        
@api_view(["POST","GET"])
def test(request):
    print(request.user.is_staff)
    if request.method == "PUT":
        abc = request.data["abc"]
        request.user.abc = abc
        return redirect("edit_profile")
    return Response("jaidfh")

        