"""
Definicion de las URL's asociadas
a la aplicacion de inventario
"""

from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login),
    path('register/', views.register),
    path('main/', views.main),
    path("recover/", views.sendPassword),
    path("showProducts/", views.showProducts),
    path("deleteProduct/", views.deleteProduct),
    path("addProduct/", views.addProduct),
    path("updateProduct/", views.updateProduct),
]
