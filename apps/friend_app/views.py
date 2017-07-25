from __future__ import unicode_literals
from ..login_app.models import Users
from .models import Friends
from django.shortcuts import render, redirect
from django.db.models import Count
from django.core.urlresolvers import reverse
from django.contrib import messages



def index(request):
    if request.session["logged_in"] == False:
        messages.error(request, "Please log in.")
        return redirect("login:index")
    context = {
        "users": Users.objects.order_by("-created_at")[:3]
    }
    return render(request, "friend_app/index.html", context)

def add(request):
    if request.session["logged_in"] == False:
        messages.error(request, "Please log in.")
        return redirect("login:index")
    context = {
        "users": Users.objects.all().exclude(id=request.session["user_id"])
    }
    return render(request, "friend_app/add.html", context)

def addfriend(request):
    if request.session["logged_in"] == False:
        messages.error(request, "Please log in.")
        return redirect("login:index")
    friend = Friends.objects.add(request.POST, request)
    if friend == False:
        return redirect("friend:add")
    return redirect("friend:show")

def show(request):
    if request.session["logged_in"] == False:
        messages.error(request, "Please log in.")
        return redirect("login:index")
    context = {
        "friends": Friends.objects.all()
    }
    return render(request, "friend_app/show.html", context)

def delete(request, id):
    if request.session["logged_in"] == False:
        messages.error(request, "Please log in.")
        return redirect("login:index")
    Friends.objects.get(id=id).delete()
    return redirect("friend:show")
