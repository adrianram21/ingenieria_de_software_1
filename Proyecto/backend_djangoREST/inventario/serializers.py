"""
Serializadores para los modelos de 
la aplicación inventario
"""

from rest_framework import serializers
from .models import Usuario
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    """
    Serializador para el 
    modelo Producto
    """

    class Meta:
        """
        Clase Meta para especificar
        el comportamiento del serializador 
        """

        model = Producto
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    """
    Serializador para el
    modelo Usuario
    """

    class Meta:
        """
        Clase Meta para especificar
        el comportamiento del serializador 
        """

        model = Usuario
        fields = ['id', 'id_organizacion', 'nombre', 'correo_electronico', 'password', 'rol']
