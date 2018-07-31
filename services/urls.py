from django.conf.urls import url,include
from . import views

app_name = 'services'

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/', views.service_detail_view, name='order_status'),
    ]