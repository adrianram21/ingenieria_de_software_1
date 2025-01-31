from rest_framework import serializers
from .models import Usuario
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

        
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'id_organizacion', 'nombre', 'correo_electronico', 'password', 'rol']
