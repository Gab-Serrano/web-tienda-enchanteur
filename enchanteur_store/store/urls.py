from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('contact/', views.contact, name="contact"),
    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('singin/', views.singin, name="singin"),

    path('manageView/', views.manageView, name="manageView"),
    path('addProduct/', views.addProduct, name="addProduct"),
    path('updateProduct/', views.updateProduct, name="updateProduct"),

    path('update_item/', views.updateItem, name="update_item"),

]
