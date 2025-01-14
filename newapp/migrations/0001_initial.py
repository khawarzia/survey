# Generated by Django 5.1.4 on 2025-01-14 15:12

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
                ('api_key', models.CharField(max_length=100, unique=True)),
                ('allowed', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='form_submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_type', models.CharField(blank=True, max_length=10, null=True)),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('comments', models.TextField(blank=True, max_length=2000, null=True)),
                ('property_type', models.CharField(blank=True, max_length=50, null=True)),
                ('apartment_type', models.CharField(blank=True, max_length=10, null=True)),
                ('fav_district', models.CharField(blank=True, max_length=250, null=True)),
                ('purpose', models.CharField(blank=True, max_length=10, null=True)),
                ('submission_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]