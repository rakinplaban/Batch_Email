from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import User
from django.core.mail import send_mail

# Create your views here.
def index(request):
    # send_mail(
    #     'Testing mail',
    #     'Here is the message',
    #     'plaban_r@yahoo.com',
    #     ['arata@relifelab.com'],
    #     fail_silently=False,
    # )
    all_users = User.objects.all()
    if request.user.is_authenticated:
        return render(request,'mailapp/index.html',{
            'all_users' : all_users,
        })
    else:
        return HttpResponseRedirect('login')

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "mailapp/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "mailapp/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def register(request):
    if request.method == "POST":
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "mailapp/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(email, email, password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "mail/register.html", {
                "message": "Email address already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "mailapp/register.html")