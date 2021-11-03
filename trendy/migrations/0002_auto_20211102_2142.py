# Generated by Django 3.2.9 on 2021-11-02 21:42

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trendy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bagproduct',
            name='image_2',
        ),
        migrations.RemoveField(
            model_name='bagproduct',
            name='image_3',
        ),
        migrations.RemoveField(
            model_name='bagproduct',
            name='image_4',
        ),
        migrations.RemoveField(
            model_name='bagproduct',
            name='image_5',
        ),
        migrations.RemoveField(
            model_name='menproduct',
            name='image_2',
        ),
        migrations.RemoveField(
            model_name='menproduct',
            name='image_3',
        ),
        migrations.RemoveField(
            model_name='menproduct',
            name='image_4',
        ),
        migrations.RemoveField(
            model_name='menproduct',
            name='image_5',
        ),
        migrations.RemoveField(
            model_name='womenproduct',
            name='image_2',
        ),
        migrations.RemoveField(
            model_name='womenproduct',
            name='image_3',
        ),
        migrations.RemoveField(
            model_name='womenproduct',
            name='image_4',
        ),
        migrations.RemoveField(
            model_name='womenproduct',
            name='image_5',
        ),
        migrations.AlterField(
            model_name='bagproduct',
            name='image_1',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='women'),
        ),
        migrations.AlterField(
            model_name='menproduct',
            name='image_1',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='women'),
        ),
        migrations.AlterField(
            model_name='womenproduct',
            name='kind',
            field=models.CharField(default='jacket, pants, sweatshirt, dress, shoes', max_length=10),
        ),
    ]
