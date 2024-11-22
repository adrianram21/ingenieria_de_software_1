from rest_framework import serializers
from .models import Prueba

class Prueba_ser(serializers.ModelSerializer):
    class Meta:
        model = Prueba
        fields = [
            'texto'
        ]