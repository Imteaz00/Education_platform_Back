from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, "index.html")

def signout(request):
    logout(request)
    messages.success(request, 'Logged out')
    return redirect("home")


def signin(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        userinfo = authenticate(username=username, password= password)

        if userinfo is not None:
            login(request, userinfo)
            return render(request, "index.html", {"username": username})

        else:
            messages.error(request, "Error in Username or Password")

    return render(request, "signin.html")

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if User.objects.filter(username=username):
            messages.error(request, "Username exists already")
            return redirect("signup")
        
        if password!= password2:
            messages.error(request, "Both password does not match")
        
        userinfo = User.objects.create_user(username, email, password)

        userinfo.save()

        messages.success(request, "Account Created Successfully!")

        return redirect("signin")

    return render(request, "signup.html")

def edit_profile(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

