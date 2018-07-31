from django.conf.urls import url,include
from . import views

app_name= 'products'

urlpatterns = [

    url(r'^error-404', views.error_404, name='error'),
    url(r'^(?P<pk>[0-9]+)/delete', views.delete_item, name='delete_item'),
    url(r'^(?P<pk>[0-9]+)/add', views.add_to_cart, name='cart'),
    url(r'^(?P<pk>[0-9]+)', views.product_detail, name='product_view'),
    url(r'^cart', views.cart_view, name='cart_list'),
    url(r'^order/confirm', views.order_cnf_view, name='order_cnf'),
    url(r'^service/solar-epc', views.solar_epc_view, name='solar_epc'),

    ]