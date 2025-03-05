"""
Vistas para la
aplicacion de inventario
"""

from django.db import IntegrityError, transaction
from django.shortcuts import get_object_or_404
from django.db.models import F
import random
import string
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UsuarioSerializer, ProductoSerializer
from .models import Usuario, Organizacion, Producto
from django.core.mail import send_mail
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError



def generar_jwt(usuario):
    """
    Funcion para la generacion 
    de Tokens JWT
    """

    refresh = RefreshToken.for_user(usuario)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@api_view(['POST'])
def login(request):
    """
    Funcion asociada al 
    proceso de login
    """

    usuario = get_object_or_404(Usuario, correo_electronico=request.data['correo_electronico'])
    if not usuario.check_password(request.data['password']):
        return Response({"error": "password invalida"}, status=status.HTTP_400_BAD_REQUEST)

    token = generar_jwt(usuario)
    serializer = UsuarioSerializer(instance=usuario)
    return Response({"token": token, "user": serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def register(request):
    nombre = request.data['nombre']
    rol = request.data['rol']
    correo_electronico = request.data['correo_electronico']
    password = request.data['password']

    if not nombre.strip():
        return Response({"error": "Error durante el proceso de registro"},
                        status=status.HTTP_400_BAD_REQUEST)
    
    if len(password) < 8:
        return Response({"error": "Error durante el proceso de registro"},
                        status=status.HTTP_400_BAD_REQUEST)

    try:
        with transaction.atomic():
            if rol == "Administrador":
                try:
                    Organizacion.objects.create(nombre_organizacion=request.data['organizacion'])
                except IntegrityError:
                    return Response({"error": "Error durante el proceso de registro"},
                                    status=status.HTTP_400_BAD_REQUEST)

            try:
                id_organizacion = Organizacion.objects.get(
                    nombre_organizacion=request.data['organizacion'])
            except Organizacion.DoesNotExist:
                return Response({"error": "Error durante el proceso de registro"},
                                status=status.HTTP_400_BAD_REQUEST)

            try:
                EmailValidator()(correo_electronico)
            except ValidationError:
                return Response({"error": "Error durante el proceso de registro"},
                                status=status.HTTP_400_BAD_REQUEST)

            usuario = Usuario.objects.create_user(
                nombre=nombre,
                rol=rol,
                id_organizacion=id_organizacion,
                correo_electronico=correo_electronico,
                password=password
            )

            serializer = UsuarioSerializer(instance=usuario)

            return Response({"mensaje": "Registro exitoso autorizado",
                             "user": serializer.data},
                            status=status.HTTP_200_OK)

    except IntegrityError:
        return Response({"error": "Error durante el proceso de registro"},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def main(request):
    """
    Funcion de prueba 
    para la conexion
    """
    return Response({"message": "Funciona"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def sendPassword(request):
    """
    Funcion para el envio
    de contraseñas
    """

    correo_electronico = request.data['correo_electronico']
    try:
        usuario = Usuario.objects.get(correo_electronico=correo_electronico)
    except Usuario.DoesNotExist:
        return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    nueva_contrasena = "".join(random.choices(string.ascii_letters + string.digits, k=10))
    usuario.set_password(nueva_contrasena)  
    usuario.save()

    send_mail(
        "Recuperacion de contrasena",
        f"Hola {usuario.nombre}, tu contrasena es {nueva_contrasena}",
        "boxy86858@gmail.com",
        [correo_electronico],
        fail_silently=False 
        )
    
    return Response({"mensaje": "Correo enviado"}, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def showProducts(request):
    """
    Funcion para mostrar
    los productos
    """

    productos = Producto.objects.filter(id_organizacion=request.data["id_organizacion"])

    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def deleteProduct(request):
    """
    Funcion para eliminar
    productos
    """

    id_producto = request.data["id_producto"]
    producto = get_object_or_404(Producto, id=id_producto)
    producto.delete()
    return Response({"mensaje": "Producto eliminado"}, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def addProduct(request):
    """
    Funcion para agregar
    productos
    """

    nombre = request.data["nombre"]
    precio = request.data["precio"]
    cantidad = request.data["cantidad"]
    categoria = request.data["categoria"]
    stock_minimo = request.data["stock_minimo"]
    id_organizacion = request.data["id_organizacion"]

    try:
        Producto.objects.create(
            nombre=nombre,
            precio=precio,
            cantidad=cantidad,
            categoria=categoria,
            stock_minimo=stock_minimo,
            id_organizacion=Organizacion.objects.get(id=id_organizacion)
        )
    except IntegrityError:
        return Response({"error": "Error al agregar producto"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"mensaje": "Producto agregado"}, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def updateProduct(request):
    """
    Funcion para actualizar
    productos
    """

    id_producto = request.data["id"]
    producto = get_object_or_404(Producto, id=id_producto)
    producto.nombre = request.data["nombre"]
    producto.precio = request.data["precio"]
    producto.cantidad = request.data["cantidad"]
    producto.categoria = request.data["categoria"]
    producto.stock_minimo = request.data["stock_minimo"]
    producto.save()
    return Response({"mensaje": "Producto actualizado"}, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def showLowStockProducts(request):
    """
    Funcion para mostrar
    los productos
    """

    productos = Producto.objects.filter(id_organizacion=request.data["id_organizacion"], cantidad__lt=F('stock_minimo'))
    

    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
