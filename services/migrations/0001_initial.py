# Generated by Django 2.0 on 2018-07-31 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_logo', models.ImageField(upload_to='')),
                ('client_name', models.CharField(max_length=30)),
                ('client_desc', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_logo', models.ImageField(upload_to='')),
                ('service_name', models.CharField(max_length=30)),
                ('service_desc', models.TextField(max_length=5000)),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Service'),
        ),
    ]
