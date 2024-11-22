from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Prueba
from .serializers import Prueba_ser

class Vista_Prueba(APIView):
    def get(self, request):
        textos = Prueba.objects.all()
        serializer = Prueba_ser(textos, many=True) 
        return Response(serializer.data)
