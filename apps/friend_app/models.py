from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
from ..login_app.models import Users

class FriendsManager(models.Manager):
    def add(self, postData, request):
        passFlag = True
        if Friends.objects.filter(name = postData['addf']):
			messages.error(request, "You have already add this person as your friend.")
			passFlag = False
        if passFlag == True:
            Friends.objects.create(name=postData["addf"], user=Users.objects.get(id=request.session["user_id"]))
        return passFlag

class Friends(models.Model):
    name = models.CharField(max_length = 100)
    user = models.ManyToManyField(Users)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = FriendsManager()
