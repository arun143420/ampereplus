from django.contrib import admin
from services.models import Client, Service

admin.site.register(Service)
admin.site.register(Client)

