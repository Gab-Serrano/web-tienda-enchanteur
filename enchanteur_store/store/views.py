from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
from . utils import cookieCart
from .forms import ProductoForm
from .models import Product
from django.shortcuts import redirect, reverse
from django.contrib import messages


def home(request):
    cartCount (request)
    context = {'cartItems': cartCount (request)}
    return render(request, 'store/index.html', context)

def login(request):
    cartCount (request)
    context = {'cartItems': cartCount (request)}
    return render(request, 'store/login.html', context)

def singin(request):
    cartCount (request)
    context = {'cartItems': cartCount (request)}
    return render(request, 'store/singin.html', context)

def contact(request):
    cartCount (request)
    context = {'cartItems': cartCount (request)}
    return render(request, 'store/contact.html', context)

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    context = {'items':items, 'order':order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']
    context = {'items':items, 'order':order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id = productId)
    order, created = Order.objects.get_or_create(customer = customer, complete = False)
    orderItem, created = OrderItem.objects.get_or_create(order = order, product = product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def cartCount (request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
    return cartItems

def manageView(request):
    context = {}
    return render(request, 'store/manageView.html', context)

def addProduct(request):
    context = {}

    form = ProductoForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto agregado correctamente')
            return redirect(reverse('addProduct'))
        else:
            messages.error(request, 'Error al agregar el producto')
    
    context['form'] = form
    return render(request, 'store/addProduct.html', context)

def updateProduct(request):
    context = {}
    return render(request, 'store/updateProduct.html', context)