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

    # ---------------------------------------PASSWORD CHANGE-----------------------------------------------------------

    url(r'^password-change/$', auth_views.password_change, {'template_name': 'registration/password_change_form.html',
                                                            'post_change_redirect': 'registration/password_change_done/'
                                                            },
        name='password_change'),

    url(r'^password-change/registration/password_change_done/$', auth_views.password_change_done,
        {'template_name': 'registration/password_change_done.html'}, name='password_change_done'),

    # ----------------------------------------PASSWORD RESET------------------------------------------------------------

    url(r'password-reset/$', PasswordResetView.as_view(template_name='accounts/password_reset_form.html',
                                                       success_url=reverse_lazy('accounts:password_reset_done'),
                                                       email_template_name='accounts/password_reset_email.html',
                                                       subject_template_name='accounts/password_reset_subject.txt'),
        name='password_reset'),

    url(r'password-reset/done/$', PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
        name='password_reset_done'),

    url(r'reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html',
                                         success_url=reverse_lazy('accounts:password_reset_complete')),
        name="password_reset_confirm"),

    url(r'^reset/complete/$', PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
        name="password_reset_complete"),

]