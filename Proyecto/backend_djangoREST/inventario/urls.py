from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'productos', views.ProductoViewSet)  

urlpatterns = [
    path('login', views.login),
    path('register', views.register),
    path('main', views.main),
    path('', include(router.urls)),  
    path('productos/stock_bajo/', views.stock_bajo, name='productos-stock-bajo'), 
]
