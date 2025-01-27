from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'id_organizacion', 'nombre', 'correo_electronico', 'password', 'rol']
