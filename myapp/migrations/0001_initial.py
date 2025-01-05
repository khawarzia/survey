# Generated by Django 5.1.4 on 2025-01-03 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='api_keys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_key', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='form_submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_type', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=300)),
                ('phone_number', models.CharField(max_length=50)),
                ('comments', models.TextField(max_length=2000)),
                ('property_type', models.CharField(max_length=50)),
                ('apartment_type', models.CharField(max_length=100)),
                ('fav_district', models.CharField(max_length=1000)),
                ('purpose', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]