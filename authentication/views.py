from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .serializers import UserinfoSerializer
from django.http import HttpResponse, HttpRequest, JsonResponse
from .models import Userinfo


# Create your views here.
@api_view(["GET", "POST"])
def home(request):
    print(request)
    if request.method == "POST":
        users = Userinfo.objects.all()
        serializer = UserinfoSerializer(users, many = True)
        return Response(serializer.data)
    return Response(str(request.user.id))

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
        
        userinfo = Userinfo.objects.create_user(username, password, email, fullname= fullname, skills = skills, is_teacher= True)

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
        
        userinfo = Userinfo.objects.create_user(username, password, email, fullname= fullname, it = interest, is_teacher = False)

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
    

@api_view(["PUT","GET"])
def edit_profile(request):
    if request.method == "PUT":
        password = request.data["password"]
        user = request.user
        if password != request.user.password:
            return Response("hacker")
        
        u = Userinfo.objects.get(id=user.id)
        u.username = request.data["username"],
        u.email = request.data["email"],
        # u.skills = request.data["skills"],
        u.phone = request.data["phone"],
        u.dob = request.data["dob"],
        # u.pic = request.data["pic"],
        u.address = request.data["address"],
        u.gender = request.data["gender"]

        u.save()
        return Response("success")
    return Response(request)

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


@api_view(["POST"])
def admin_pass(request):
    pass
    # if request.method == "POST":
    #     superpass = request.data["superpass"]
    #     if superpass == "Hehheboy":
    #         request.user.is_staff = True
    #         return redirect("create_admin")
    #     myuser.user_permissions.add(permission, permission, ...)
    #     myuser.user_permissions.remove(permission, permission, ...)

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

        