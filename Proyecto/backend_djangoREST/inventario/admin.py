"""
Registro de los modelos en el 
panel de administración de Django.
"""

from django.contrib import admin
from .models import Usuario, Organizacion, Producto, Movimiento

admin.site.register(Organizacion)
admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Movimiento)
