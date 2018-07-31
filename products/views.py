from django.shortcuts import render
from products.models import Product, Cart, Checkout
from accounts.models import ContactUs, GuestUser
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from accounts.forms import ProfileForm
from django.contrib import messages
from manager.models import CartManager
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.core.mail import send_mail
from services.models import Service


def homepage(request):
    services_list = Service.objects.all()
    return render(request, 'products/home.html', {'services_list':services_list})


def contact_us_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact_us = ContactUs()
        contact_us.name = name
        contact_us.email = email
        contact_us.subject = subject
        contact_us.message = message
        contact_us.save()
        messages.success(request, "your Query Submitted Successfully ")
        send_mail(
            subject=subject,
            message="Name:" + " " + name + '\n\n' + "sender:" + " " + email + '\n' + message,
            from_email=email,
            recipient_list=['arun.57-cse-15@mietjammu.in'],
            fail_silently=False,
            )

        return HttpResponseRedirect('/contact_us')

    else:
        return render(request, 'products/contact.html', {})


def about_view(request):
    return render(request, 'products/about.html', {})


def products_list_view(request, pk=None):
    product_list = Product.objects.all()
    service_list = Service.objects.all()
    context = {
        'products_list': product_list,
        'services_list': service_list
    }
    return render(request, 'products/services_products_list.html', context)


def product_detail(request,pk):
    if request.method =='GET':
        product = get_object_or_404(Product, pk=pk)
        context = {
            'product': product
        }
        return render(request, 'products/product_detail.html', context)

    else:
        return HttpResponseRedirect('/')


@csrf_exempt
def add_to_cart(request, pk):
    menu = get_object_or_404(Product, pk=pk)
    request.session['user'] = 'guest'
    if request.method == "POST":
        total_cost = request.POST.get("total_cost", None)
        quantity = request.POST.get("quantity", None)
        actual = request.POST.get("actual", None)
        if request.user.is_authenticated:
            cart = Cart()
            cart.product_prices = total_cost
            cart.quantity = quantity
            cart.product = menu
            cart.user = request.user
            cart.actual_prices = actual
            cart.save()
            return JsonResponse({'menu': cart.product.prod_name})
        else:
            unique_id = request.session._session_key
            cart = Cart()
            cart.product_prices = total_cost
            cart.quantity = quantity
            cart.product = menu
#           cart.user = request.user
            cart.actual_prices = actual
            cart.unique_key = unique_id
            cart.save()
            print(unique_id)
            return JsonResponse({'menu': menu.prod_name})

    else:
        return HttpResponseRedirect('/')


def cart_view(request):
    template_name = 'products/cart.html'
    if request.method == 'GET':
        if request.user.is_authenticated:
            form = ProfileForm(instance=request.user.profile or None)
            cart_items = Cart.objects.filter(user=request.user)
            context = {
                'cart_items': cart_items,
                'form':form
                }
            return render(request, 'products/cart.html', context)
        else:
            form = GuestUser()
            unique_key = request.session.session_key
            cart_items = Cart.objects.filter(unique_key=unique_key)
            context = {
                'cart_items': cart_items,
                'form': form
            }

            return render(request, 'products/cart.html', context)

    else:
        if request.user.is_authenticated:
            form = ProfileForm(request.POST, instance=request.user.profile)
            cart_items = Cart.objects.filter(user=request.user)
            context = {
                'cart_items': cart_items,
                'form': form,
            }

            if form.is_valid():
                profile = form.save(commit=False)
                profile.save()
                messages.success(request, "Your address details added Successfully.")
                return HttpResponseRedirect('/products/cart')
            return render(request, template_name, context)
        else:
            pass


@csrf_exempt
def delete_item(request, pk):
        item = get_object_or_404(Cart, pk=pk)
        product_name = item.product.prod_name
        item.delete()
        messages.success(request, product_name + " " + "deleted from your cart")
        return HttpResponseRedirect('/products/cart')


def order_cnf_view(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            order_no = request.POST['order_no']
            payment = request.POST['payment']
            total_price = request.POST['total_price']
            checkout = Checkout()
            checkout.user = request.user
            checkout.order_id = order_no
            checkout.total_price = total_price
            checkout.payment = payment
            checkout.save()

            for item in Cart.objects.filter(user=request.user):
                manager = CartManager()
                item.checkout = checkout
                manager.product = item.product
                manager.user = item.user
                manager.checkout = checkout
                manager.quantity = item.quantity
                manager.actual_prices = item.actual_prices
                manager.product_prices = item.product_prices
                item.save()
                manager.save()

            context = {
                'order_id': order_no,
                'total_price': total_price
            }
            return render(request, 'products/order_placed.html', context)
        else:
            order_no = request.POST['order_no']
            payment = request.POST['payment']
            total_price = request.POST['total_price']
            checkout = Checkout()
            checkout.order_id = order_no
            checkout.total_price = total_price
            checkout.payment = payment
            checkout.save()
            guest = GuestUser()
            guest.checkout = checkout
            guest.name = request.POST['guest_name']
            guest.email = request.POST['guest_email']
            guest.phone = request.POST['guest_number']
            guest.zipcode = request.POST['guest_zipcode']
            guest.area = request.POST['guest_area']
            guest.address = request.POST['guest_address']
            guest.save()

            unique_id = request.session.session_key
            for item in Cart.objects.filter(unique_key=unique_id):
                item.checkout = checkout
                manager = CartManager()
                manager.product = item.product
                manager.checkout = checkout
                manager.quantity = item.quantity
                manager.actual_prices = item.actual_prices
                manager.product_prices = item.product_prices
                item.save()
                manager.save()

            context = {
                'order_id': order_no,
                'total_price': total_price
            }
            return render(request, 'products/order_placed.html', context)

    else:
        return HttpResponseRedirect('/')


def error_404(request):
    return HttpResponse('ERRROR')


def error_500(request):
    pass


def solar_epc_view(request):
    return render(request, 'products/solar_epc.html', {})
