from django.db import models
from multiselectfield import MultiSelectField
from django.conf import settings


comm_format = (('wifi', 'WIFI'),
              ('sim', 'SIM'),
              ('ethernet', 'Ethernet'),
              ('bluetooth', 'Bluetooth'),
              ('lora', 'LORA'),
               )

port_type_choices = (('U-ART', 'U-ART'),
                     ('RS232', 'RS232'),
                     ('RS485', 'RS485'),
                     )

power_supplies = (('V1', '12V'),
                  ('V2', '5V'),
                  ('V3', '3.3V')
                  )


class Product(models.Model):
    prod_name = models.CharField(max_length=30, null=False)
    prod_desc = models.TextField(max_length=500, null=False)
    available = models.BooleanField(default=True)
    communication_format = MultiSelectField(choices=comm_format)
    PortType = MultiSelectField(choices=port_type_choices)
    PowerSource = MultiSelectField(choices=power_supplies)
    storage = models.BooleanField(default=False)
    antenna = models.BooleanField(default=False)
    rtc = models.BooleanField(default=False)
    prod_price = models.FloatField(max_length=10, default=0)
    sell_price = models.FloatField(max_length=10, default=0)

    def __str__(self):
        return str(self.prod_name)


class Checkout(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    order_id = models.CharField(max_length=20)
    order_time = models.DateTimeField(auto_now=True)
    payment = models.CharField(max_length=20)
    total_price = models.DecimalField(max_digits=30, decimal_places=2, default=0)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.order_id)


class Cart(models.Model):
    unique_key = models.CharField(max_length=20 ,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    checkout = models.ForeignKey(Checkout, on_delete=models.CASCADE, null=True)
    product_prices = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    actual_prices = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    add_time = models.DateTimeField(auto_now=True)
    quantity = models.CharField(max_length=20, default=0)

    def __str__(self):
        return str(self.product)

