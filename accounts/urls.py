from django.conf.urls import url
from . import views
from accounts.forms import CustomAuthForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy


app_name = 'accounts'

urlpatterns = [

    url(r'^signup', views.signup_view, name='aa'),
    url(r'^login/$', auth_views.login, name='login', kwargs={"authentication_form": CustomAuthForm}),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^profile$', views.ProfileView, name='profile'),
    url(r'^profile/edit$', views.profile_edit, name='profile-edit'),




    ]