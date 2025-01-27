from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .serializers import UsuarioSerializer
from .models import Usuario
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .models import Usuario, Organizacion
from django.db import IntegrityError
from rest_framework_simplejwt.authentication import JWTAuthentication

def generar_jwt(usuario):
    refresh = RefreshToken.for_user(usuario)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@api_view(['POST'])
def login(request):
    usuario = get_object_or_404(Usuario, correo_electronico=request.data['correo_electronico'])
    if(not usuario.check_password(request.data['password'])):
        return Response({"error": "password invalida"}, status=status.HTTP_400_BAD_REQUEST)

    else:
        token = generar_jwt(usuario)

        serializer = UsuarioSerializer(instance=usuario)

        return Response({"token": token, "user": serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def register(request):
    nombre = request.data['nombre']
    rol = request.data['rol']
    correo_electronico = request.data['correo_electronico']
    password = request.data['password']
    
    if (rol == "Administrador"):
        try:
            Organizacion.objects.create(nombre_organizacion = request.data['organizacion'])
        except IntegrityError:
            return Response({"error": "Ya hay una organizacion con este nombre"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        id_organizacion = Organizacion.objects.get(nombre_organizacion = request.data['organizacion'])
    except Organizacion.DoesNotExist:
        return Response({"error": "La organizacion no existe"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        usuario = Usuario.objects.create_user(
            nombre = nombre,
            rol = rol,
            id_organizacion = id_organizacion,
            correo_electronico = correo_electronico,
            password = password
        )
    except IntegrityError:
        return Response({"error": "El correo electronico ya esta en uso"}, status=status.HTTP_400_BAD_REQUEST)


    serializer = UsuarioSerializer(instance=usuario)

    return Response({"mensaje": "Registro existoso autorizado", "user": serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def main(request):
    return Response({"message": "Funciona"}, status=status.HTTP_200_OK)