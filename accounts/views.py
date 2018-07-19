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


def signup_view(request):
    template_name = 'accounts/signup.html'

    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form1 = form.save(commit=False)
            email = form.cleaned_data['email']
            if email and User.objects.filter(email=email).exists():
                messages.success(request, "Email address"+" "+email+" "+"Already Registered.")
                return render(request, template_name, {'form': form})
            form1.save()
            messages.success(request, "Your account has been created Successfully")
            return redirect('/accounts/login')
        return render(request,template_name, {'form': form})
    else:
        form = SignUpForm
        return render(request, template_name, {'form': form})


@login_required
@csrf_exempt
def ProfileView(request):
    template_name = 'products/cart.html'
    if request.method == "POST":
        address = request.POST.get("address", None)
        phone = request.POST.get("phone", None)
        zipcode = request.POST.get("zipcode", None)
        area = request.POST.get("area", None)
        profile = get_object_or_404(Profile, user=request.user)
        profile.user = request.user
        profile.address = address
        profile.phone = phone
        profile.zipcode = zipcode
        profile.area = area
        profile.tc = True
        profile.save()
        return JsonResponse({'profile': profile.user.username})


    else:
        form = ProfileForm(instance=request.user.profile or None)
        context ={
            'form': form,
        }

        return render(request, template_name, context)


@login_required
def profile_edit(request):
    profile = get_object_or_404(Profile, user=request.user)
    profile.tc = False
    profile.save()
    return HttpResponseRedirect('/products/cart')




