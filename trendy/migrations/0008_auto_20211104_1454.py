# Generated by Django 3.2.9 on 2021-11-04 14:54

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trendy', '0007_auto_20211104_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='kind',
        ),
        migrations.RemoveField(
            model_name='product',
            name='new',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]