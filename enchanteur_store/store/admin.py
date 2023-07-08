from django.contrib import admin
from .models import *
from login.models import Profile

admin.site.register(Profile)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

""" 
superuser: admin-store
email: admin-store@enchanteur.cl
password: admin147 
"""
