from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class ContactUs(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return str(self.name)+' ' + ' ' + str(self.subject)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, blank=False)
    area = models.CharField(max_length=30, blank=False)
    address = models.CharField(max_length=60, blank=False)
    zipcode = models.CharField(max_length=6, blank=False)
    tc = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
