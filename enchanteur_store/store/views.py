from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
from . utils import cookieCart, guestOrder
from .forms import ProductoForm
from .models import Product
from django.shortcuts import redirect, reverse
from django.contrib import messages
import datetime


def home(request):
    cartCount (request)
    context = {'cartItems': cartCount (request)}
    return render(request, 'store/index.html', context)

def login(request):
    cartCount (request)
    context = {'cartItems': cartCount (request)}
    return render(request, 'store/login.html', context)

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

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
 
    else:
        customer, order = guestOrder(request, data)
    
    total = int(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
            order.complete = True
    order.save()

    ShippingAddress.objects.create(
                customer = customer,
                order = order,
                address = data['shipping']['address'],
                city = data['shipping']['city'],
                state = data['shipping']['state'],
                country = data['shipping']['country'],
                zipcode = data['shipping']['zipcode'],
            )

    return JsonResponse('Payment complete!', safe=False)

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
    products = Product.objects.all()
    context = {'products': products,}
    return render(request, 'store/manageView.html', context)

def addProduct(request):
    context = {}

    form = ProductoForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto agregado correctamente')
            context['success_message'] = True  # Agregar esta línea
            return redirect('addProduct')
        else:
            print(form.errors)  # Imprime los errores en la consola
            messages.warning(request, 'Error al agregar el producto')
    
    context['form'] = form

    return render(request, 'store/addProduct.html', context)

def updateProduct(request):
    context = {}
    return render(request, 'store/updateProduct.html', context)