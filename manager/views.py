from django.shortcuts import render
from products.models import Product, Cart, Checkout
from accounts.models import ContactUs
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from accounts.forms import ProfileForm
from django.contrib import messages
from manager.models import CartManager
from django.http import HttpResponseRedirect, JsonResponse
from manager.models import CartManager


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
            context = {
                'checkout': checkout
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