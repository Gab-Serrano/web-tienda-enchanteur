from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm
from store.views import cartCount

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
