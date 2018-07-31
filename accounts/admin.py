from django.contrib import admin
from accounts.models import ContactUs, Profile, GuestUser

admin.site.register(ContactUs)
admin.site.register(Profile)
admin.site.register(GuestUser)


