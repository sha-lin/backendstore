# Generated by Django 3.2.9 on 2021-11-04 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trendy', '0008_auto_20211104_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]