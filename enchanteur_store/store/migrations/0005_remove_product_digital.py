# Generated by Django 4.2.1 on 2023-06-10 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_order_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='digital',
        ),
    ]
