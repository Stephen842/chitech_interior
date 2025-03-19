# Generated by Django 5.0.6 on 2025-03-19 21:27

import django_countries.fields
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='MyUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='NG', unique=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'My Users',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('price', models.IntegerField(default=0)),
                ('discount_price', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField()),
                ('condition', models.CharField(blank=True, max_length=20, null=True)),
                ('color', models.CharField(blank=True, max_length=20, null=True)),
                ('material', models.CharField(blank=True, max_length=50, null=True)),
                ('dimensions', models.CharField(blank=True, max_length=100, null=True)),
                ('weight', models.CharField(blank=True, max_length=50, null=True)),
                ('brand', models.CharField(blank=True, max_length=50, null=True)),
                ('stock_availability', models.BooleanField(default=True)),
                ('usage_type', models.CharField(blank=True, choices=[('indoor', 'Indoor'), ('outdoor', 'Outdoor'), ('both', 'Both')], max_length=50, null=True)),
                ('style', models.CharField(blank=True, max_length=50, null=True)),
                ('assembly_required', models.BooleanField(default=False)),
                ('warranty', models.CharField(blank=True, max_length=50, null=True)),
                ('featured', models.BooleanField(default=False)),
                ('image_0', models.ImageField(upload_to='products/')),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('category', models.ManyToManyField(related_name='products', to='furniture.category')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
    ]
