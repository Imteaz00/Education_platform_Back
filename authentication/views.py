from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .serializers import UserinfoSerializer
from django.http import HttpResponse, HttpRequest, JsonResponse
from .models import Teacher, Student


# Create your views here.
@api_view(["GET", "POST"])
def home(request):
    if request.method == "POST":
        users = User.objects.all()
        serializer = UserinfoSerializer(users, many = True)
        return Response(serializer.data)

@api_view(["POST"])
def signout(request):
    if request.method == "POST":
        logout(request)
        return Response("bye")


@api_view(["POST"])
def signin(request):
    if request.method == "POST":
        username = request.data["username"]
        password = request.data["password"]

        userinfo = authenticate(username=username, password= password)

        if userinfo is not None:
            login(request, userinfo)
            return Response("welcome")


@api_view(["POST"])
def teacher_signup(request):
    if request.method == "POST":
        username = request.data["username"]
        fullname = request.data["fullname"]
        email = request.data["email"]
        password = request.data["password"]
        password2 = request.data["cpass"]
        skills = request.data["skills"]


        if User.objects.filter(username=username):
            return Response("f")
        
        if password!= password2:
            return Response("g")
        
        userinfo = Teacher.objects.create_user(username, password, email, fullname= fullname, skills = skills)

        userinfo.save()

        return Response("gg")
    return Response("Do")

@api_view(["POST", "GET"])
def signup(request):
    if request.method == "POST":
        username = request.data["username"]
        fullname = request.data["fullname"]
        email = request.data["email"]
        password = request.data["password"]
        password2 = request.data["cpass"]
        interest = request.data["it"]


        if User.objects.filter(username=username):
            return Response("f")
        
        if password!= password2:
            return Response("g")
        
        userinfo = Student.objects.create_user(username, password, email, fullname= fullname, it = interest)

        userinfo.save()

        return Response("gg")
    return Response("Do")

@api_view(["POST"])
def create_admin(request):
    if request.method == "POST":
        username = request.data["username"]
        # fullname = request.data["fullname"]
        email = request.data["email"]
        # it = request.it["it"]
        password = request.data["password"]
        password2 = request.data["password2"]


        if User.objects.filter(username=username):
            messages.error(request, "Username exists already")
            return redirect("create_admin")
        
        if password!= password2:
            messages.error(request, "Both password does not match")
            return redirect("create_admin")
        
        userinfo = User.objects.create_superuser(username, email, password)

        userinfo.save()
        
        userinfo = authenticate(username=username, password=password)
        login(request, userinfo)
        messages.success(request, "Account Created Successfully!")
        return redirect("home")
    

@api_view(["PUT"])
def edit_profile(request):
    if request.method == "PUT":
        password = request.data["password"]
        user = request.user
        if password != request.user.password:
            return Response("hacker")
        

        userinfo = User.objects.update(
        username = request.data["username"],
        email = request.data["email"],
        interest = request.data["it"],
        phone = request.data["phone"],
        dob = request.data["dob"],
        pic = request.data["pic"],
        address = request.data["address"],
        gender = request.data["gender"]
        )

        userinfo.save()
        return Response("succerss")

@api_view(["POST"])
def changePass(request):
    if request.method == "POST":
        pass1 = request.data["pass1"]
        pass2 = request.data["pass2"]
        username = request.user.pk
        user = User.objects.get(pk = username)

        if pass1 != pass2:
            return Response("g")

        user.set_password(pass1)
        user.save()


# @api_view(["POST"])
# def admin_pass(request):
#     if request.method == "POST":
#         superpass = request.data["superpass"]
#         if superpass == "Hehheboy":
#             request.user.is_staff = True
#             return redirect("create_admin")
#         myuser.user_permissions.add(permission, permission, ...)
#         myuser.user_permissions.remove(permission, permission, ...)

# @api_view(["POST","GET"])       
# def teacher(request, house_id):
#     teacher = Teacher.objects.get(pk = house_id)
#     if request.user.is_authenticated:
#         cart_items = Cart_item.objects.filter(cart=Cart.objects.get(manush=request.user))
#         for item in cart_items:
#             if item.house == house:
#                 in_cart = True
#                 break
        
@api_view(["POST","GET"])
def test(request):
    return Response("jaidfh")

        