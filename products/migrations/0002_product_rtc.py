# Generated by Django 2.0.6 on 2018-07-08 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rtc',
            field=models.BooleanField(default=False),
        ),
    ]
