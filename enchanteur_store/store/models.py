from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 200, null=True)
    last_name = models.CharField(max_length = 200, null=True)
    email = models.CharField(max_length = 200, null=True)

    def __str__(self):
        return str(self.id)

class Product(models.Model):
    name = models.CharField(max_length = 50, null=True)
    description = models.CharField(max_length = 200, null=True)
    price = models.IntegerField()
    image = models.ImageField(null=True, blank=True, upload_to='products-img/')
    featured = models.BooleanField(default=False, null=True, blank=False)

    @property
    def imageURL(self):
        if self.image:
            try:
                url = self.image.url
            except:
                url = ''
        else:
            url = ''
        return url

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_order = models.DateTimeField(auto_now_add= True),
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length = 200, null=True)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    data_added = models.DateTimeField(auto_now_add= True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length = 200, null=True)
    city = models.CharField(max_length = 200, null=True)
    state = models.CharField(max_length = 200, null=True)
    country = models.CharField(max_length = 200, null=True)
    zipcode = models.CharField(max_length = 200, null=True)
    data_added = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.address
    
