from django.db import models


class Service(models.Model):
    service_logo = models.ImageField(blank=False)
    service_name = models.CharField(max_length=30, blank=False)
    service_desc = models.TextField(max_length=5000, blank=False)

    def __str__(self):
        return str(self.service_name)


class Client(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    client_logo = models.ImageField(blank=False)
    client_name = models.CharField(max_length=30, blank=False)
    client_desc = models.TextField(max_length=2000, blank=False)

    def __str__(self):
        return str(self.client_name) + " " + "using" + " " + str(self.service)