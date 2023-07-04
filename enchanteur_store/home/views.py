from django.shortcuts import render
from store.views import cartCount

def home(request):
    cartCount (request)
    context = {'cartItems': cartCount (request)}
    return render(request, 'home/index.html', context)

def aboutUs(request):
    cartCount (request)
    context = {'cartItems': cartCount (request)}
    return render(request, 'home/aboutUs.html', context)
