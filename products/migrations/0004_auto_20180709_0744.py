# Generated by Django 2.0.6 on 2018-07-09 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20180709_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='checkout',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Checkout'),
        ),
    ]