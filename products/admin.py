from django.contrib import admin
from products.models import Product,Checkout,Cart

admin.site.register(Product)
admin.site.register(Checkout)
admin.site.register(Cart)
