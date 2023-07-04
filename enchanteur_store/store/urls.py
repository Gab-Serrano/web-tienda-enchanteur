from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('login/', views.login, name="login"),
    path('contact/', views.contact, name="contact"),
    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('singin/', views.singin, name="singin"),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
]
