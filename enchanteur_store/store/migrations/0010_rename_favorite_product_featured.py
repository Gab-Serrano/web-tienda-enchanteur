# Generated by Django 4.2.1 on 2023-07-07 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_product_favorite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='favorite',
            new_name='featured',
        ),
    ]