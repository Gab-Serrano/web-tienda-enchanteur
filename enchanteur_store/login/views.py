from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm
from store.views import cartCount
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.address = form.cleaned_data.get('address')
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.city = form.cleaned_data.get('city')
            user.profile.state = form.cleaned_data.get('state')
            user.profile.zip_code = form.cleaned_data.get('zip_code')
            user.profile.country = form.cleaned_data.get('country')
            user.profile.date_of_birth = form.cleaned_data.get('date_of_birth')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()

    context = {'cartItems': cartCount (request), 'form': form}
    return render(request, 'login/register.html', context)

def signin(request):
    context = {'cartItems': cartCount (request)}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate (request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
    return render(request, 'login/sign-in.html', context)

def signout(request):
    logout(request)
    return redirect('home')

def signin_staff(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if autenticar_staff(request, username, password):
            return redirect('staff')
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
    return render(request, 'login/sign-in-staff.html')

def autenticar_staff(request, user, password):
    user = authenticate (request, username=user, password=password)
    if user is not None and user.is_staff:
        login(request, user)
        return True
    else:
        return False

