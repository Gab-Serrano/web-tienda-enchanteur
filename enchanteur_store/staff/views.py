from django.shortcuts import render, redirect, get_object_or_404
from staff.forms import addProductForm
from store.models import Product
from django.contrib import messages

def staff(request):
    products = Product.objects.all()
    context = {'products': products,}
    return render(request, 'staff/staff.html', context)

def addProduct(request):
    context = {}

    form = addProductForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto agregado correctamente')
            context['success_message'] = True  # Agregar esta línea
            return redirect('addProduct')
        else:
            print(form.errors)  # Imprime los errores en la consola
            messages.error(request, 'Error al agregar el producto')
    
    context['form'] = form

    return render(request, 'staff/addProduct.html', context)

def editProduct(request, pk):
    context = {}

    obj = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto editado correctamente')
            context['success_message'] = True  # Agregar esta línea
            return redirect('manageView')
        else:
            print(form.errors)  # Imprime los errores en la consola
            messages.warning(request, 'Error al editar el producto')
    
    context['form'] = form

    return render(request, 'staff/editProduct.html', context)

def deleteProduct(request, pk):
    producto = get_object_or_404(Product, pk=pk)
    producto.delete()
    return redirect('manageView')
