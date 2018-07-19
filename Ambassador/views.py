from django.shortcuts import render, redirect
from accounts.forms import ProfileForm
from accounts.models import Profile
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import SignUpForm #ProfileForm,SignUpEditForm
from django.contrib import messages
from django.contrib.auth.admin import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,JsonResponse
from accounts.models import Profile
from django.contrib.auth.views import login,UserModel
from django.core.mail import send_mail
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from Ambassador.forms import AmbassadorForm



@login_required
def ambassador_info_view(request):
    if request.method == 'POST':
        check = request.POST['check']
        print(check)

        if check == 'true':
            u_address = request.POST['address']
            u_zip = request.POST['zipcode']
            u_area = request.POST['area']
            u_phone = request.POST['phone']
            profile = get_object_or_404(Profile, user = request.user)
            profile.address = u_address
            profile.zipcode = u_zip
            profile.phone = u_phone
            profile.area = u_area
            profile.tc = True
            form = AmbassadorForm(request.POST)
            if form.is_valid():
                u_form = form.save(commit=False)
                u_form.user = request.user
                u_form.save()
                profile.save()
                return render(request, 'Ambassador/campus_amb_form.html', {'form': form})

        elif check == 'false':
            form = AmbassadorForm(request.POST)
            if form.is_valid():
                u_form = form.save(commit = False)
                u_form.user = request.user
                u_form.save()
                return render(request, 'Ambassador/campus_amb_form.html', {'form': form})

    else:
        form = AmbassadorForm()
        return render(request, 'Ambassador/campus_amb_form.html', {'form': form})




