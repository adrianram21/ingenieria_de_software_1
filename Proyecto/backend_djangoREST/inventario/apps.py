"""
Este archivo define la configuración de 
la aplicación 'inventario' para el proyecto Django.
"""

from django.apps import AppConfig


class InventarioConfig(AppConfig):
    """
    Configuración de la 
    aplicación Inventario
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inventario'
