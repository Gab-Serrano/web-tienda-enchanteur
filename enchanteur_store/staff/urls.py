from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('staff/', views.staff, name="staff"),
    path('addProduct/', views.addProduct, name="addProduct"),
    path('editProduct/<int:pk>', views.editProduct, name="editProduct"),
    path('deleteProduct/<int:pk>', views.deleteProduct, name="deleteProduct"),
]