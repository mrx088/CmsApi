# Generated by Django 5.0.3 on 2024-03-15 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/%Y/%m/%d/'),
        ),
    ]
