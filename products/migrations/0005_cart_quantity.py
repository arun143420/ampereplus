# Generated by Django 2.0.6 on 2018-07-09 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20180709_0744'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
