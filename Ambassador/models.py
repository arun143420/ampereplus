from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Ambassador(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    college_address = models.CharField(max_length=50)
    college_name = models.CharField(max_length=100)
    college_year = models.CharField(max_length=30)
    skills = models.CharField(max_length=100)
    motive = models.TextField(max_length=1000)
    responsibility = models.TextField(max_length=1000)
