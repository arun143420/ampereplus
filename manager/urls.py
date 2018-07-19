from django.conf.urls import url,include
from . import views

app_name = 'manager'

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/status', views.order_status_view, name='order_status'),
    url(r'^all_orders', views.orders_list_view, name='all_orders'),
    url(r'^order/(?P<pk>[0-9]+)/', views.order_detail_view, name='order_detail'),


]