
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Users

def index(request):
    if "logged_in" not in request.session:
        request.session["logged_in"] = False
    return render(request, "login_app/index.html")

def register(request):
    if request.POST:
        user_check = Users.objects.register(request.POST, request)
    else:
        messages.error(request, "No information to process.")
    return redirect("login:index")

def login(request):
    if request.session["logged_in"]:
        return redirect("friend:index")
    if request.POST:
        user_check = Users.objects.login(request.POST, request)
        if "user" in user_check:
            request.session["user_id"] = user_check["user"][0].id
            request.session["first_name"] = user_check["user"][0].first_name
            request.session["logged_in"] = True
            return redirect("friend:index")
        else:
            request.session["logged_in"] = False
    else:
        messages.error(request, "No login information.")
    return redirect("login:index")

def logout(request):
    request.session.flush()
    return redirect("login:index")
