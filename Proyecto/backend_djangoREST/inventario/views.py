"""
Vistas para la
aplicacion de inventario
"""

from django.db import IntegrityError, transaction
from django.shortcuts import get_object_or_404
from django.db.models import F
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UsuarioSerializer, ProductoSerializer
from .models import Usuario, Organizacion, Producto
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


class ProductoViewSet(viewsets.ModelViewSet):
    """
    CRUD de productos para el inventario.
    Solo los administradores pueden modificar datos.
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Permitir solo a los administradores registrar nuevos productos.
        """
        if request.user.rol != "Administrador":
            return Response({"error": "No tienes permisos para agregar productos"},
                            status=status.HTTP_403_FORBIDDEN)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Permitir solo a los administradores modificar productos.
        """
        if request.user.rol != "Administrador":
            return Response({"error": "No tienes permisos para modificar productos"},
                            status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Permitir solo a los administradores eliminar productos.
        """
        if request.user.rol != "Administrador":
            return Response({"error": "No tienes permisos para eliminar productos"},
                            status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)

# API para visualizar productos con stock bajo
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def stock_bajo(request):
    """
    Retorna los productos cuyo stock es inferior al mínimo definido.
    """
    productos_bajo_stock = Producto.objects.filter(cantidad__lt=F('stock_minimo'))
    serializer = ProductoSerializer(productos_bajo_stock, many=True)
    return Response(serializer.data,
                    status=status.HTTP_200_OK)
