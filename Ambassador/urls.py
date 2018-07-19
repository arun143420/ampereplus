from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from Ambassador import views

app_name = 'Ambassador'

urlpatterns = [

    url(r'^campus_ambassador', views.ambassador_info_view, name='campus_amb'),


]