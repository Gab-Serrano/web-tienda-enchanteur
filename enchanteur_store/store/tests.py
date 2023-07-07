""" py manage.py shell """

from django.test import TestCase
from store.models import Product
import os

products = Product.objects.all()

for product in products:
    print(product.image.name)

for product in products:
    old_path = product.image.name
    base_path = 'products-img/'
    new_path = os.path.join(base_path, os.path.basename(old_path))
    product.image.name = new_path
    product.save()


print('------------------')

for product in products:
    print(product.image.name)