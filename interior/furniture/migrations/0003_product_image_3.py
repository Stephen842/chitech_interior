# Generated by Django 5.0.6 on 2025-03-16 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furniture', '0002_remove_product_category_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
    ]
