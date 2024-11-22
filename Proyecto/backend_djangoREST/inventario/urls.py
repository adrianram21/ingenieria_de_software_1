from django.urls import path
from .views import Vista_Prueba

urlpatterns = [
    path('texto/', Vista_Prueba.as_view(), name='textos-lista')
]