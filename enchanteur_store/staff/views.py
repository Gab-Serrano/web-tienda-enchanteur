from django.shortcuts import render, redirect, get_object_or_404
from staff.forms import ProductForm
from store.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

def is_staff(user):
    return user.is_staff

@login_required(login_url='signin_staff')
@user_passes_test(is_staff, login_url='signin_staff')
def staff(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, "staff/staff.html", context)

@login_required(login_url='signin_staff')
@user_passes_test(is_staff, login_url='signin_staff')
def addProduct(request):
    context = {}

    form = ProductForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Producto agregado correctamente")
            context["success_message"] = True  # Agregar esta línea
            return redirect("staff")
        else:
            messages.error(request, "Error al agregar el producto")

    context["form"] = form

    return render(request, "staff/addProduct.html", context)

@login_required(login_url='signin_staff')
@user_passes_test(is_staff, login_url='signin_staff')
def editProduct(request, pk):
    context = {}
    obj = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=obj)

    image_url = obj.imageURL
    context['image_url'] = image_url

    if request.method == "POST":
        if form.is_valid():
            objectForm = form.save(commit=False)

            file = request.FILES.get('id_image')
            if file:
                objectForm.image = file
            
            featured = request.POST.get('featured')
            objectForm.featured = featured == 'on'

            objectForm.save()
            messages.success(request, "Producto editado correctamente")
            context["success_message"] = True  # Agregar esta línea
            return redirect("staff")
        else:
            messages.error(request, "Error al editar el producto")

    context["form"] = form

    return render(request, "staff/editProduct.html", context)

@login_required(login_url='signin_staff')
@user_passes_test(is_staff, login_url='signin_staff')
def deleteProduct(request, pk):
    context = {}
    product = get_object_or_404(Product, pk=pk)
    context['product'] = product

    if request.method == "POST":
        product.delete()
        messages.success(request, "Producto eliminado correctamente")
        return redirect("staff")
    return render(request,"staff/deleteProduct.html", context)
