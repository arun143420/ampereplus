from django.shortcuts import render
from products.models import Checkout
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from accounts.models import GuestUser
from django.contrib.auth.models import User



@login_required
def orders_list_view(request):
    if request.method == 'GET':
        if request.user.is_superuser or request.user.is_staff:
            checkout = Checkout.objects.all().order_by("-order_time")
            context = {
                'all_checkouts': checkout
            }
            return render(request, 'manager/all_orders.html', context)


@login_required
def order_detail_view(request, pk):
    if request.method == 'GET':
        if request.user.is_superuser or request.user.is_staff:
            checkout = get_object_or_404(Checkout, pk=pk)
            guest = GuestUser.objects.filter(checkout=checkout).exists()
            print(guest)
            if guest:
                guest_data = get_object_or_404(GuestUser, checkout=checkout)
                context = {
                    'checkout': checkout,
                    'guest': guest_data

                }
                return render(request, 'manager/order_detail.html', context)
            else:
                context = {
                    'checkout': checkout,
                }
                return render(request, 'manager/order_detail.html', context)


@login_required
def order_status_view(request, pk):
    if request.method == 'POST':
        if request.user.is_superuser or request.user.is_staff:
            status = request.POST['status']
            manger = get_object_or_404(Checkout, pk=pk)
            if status == 'true':
                manger.status = True
                manger.save()
                return HttpResponseRedirect('/manager/all_orders')
            elif status == 'false':
                manger.status = False
                manger.save()
                return HttpResponseRedirect('/manager/all_orders')
        else:
            HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


@login_required
def users_list_view(request):
    if request.method == 'GET':
        if request.user.is_superuser or request.user.is_staff:
            all_users = User.objects.filter().exclude(username = request.user.username)
            guest_users = GuestUser.objects.all()
            context = {'all_users': all_users,
                       'guest_users': guest_users}
            return render(request, 'manager/all_users.html', context)

