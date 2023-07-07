from django.shortcuts import render
from store.views import cartCount
from store.models import Product

def home(request):
    products = Product.objects.all()
    cartCount (request)
    context = {'cartItems': cartCount (request), 'products': products}
    return render(request, 'home/index.html', context)

def aboutUs(request):
    cartCount (request)
    context = {'cartItems': cartCount (request)}
    return render(request, 'home/aboutUs.html', context)
