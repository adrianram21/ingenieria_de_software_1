"""
Creacion del modelo
para la base de datos
"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class Organizacion(models.Model):
    """
    Definición de la 
    clase organización
    """
    nombre_organizacion = models.CharField(max_length=100, unique=True)

    class Meta:
        """
        Especificacion del plural
        y singular de Organizacion
        """
        verbose_name = "Organización"
        verbose_name_plural = "Organizaciones"

    def __str__(self):
        return f"{self.nombre_organizacion}"

class UsuarioManager(BaseUserManager):
    """
    Definición de UsuarioManager
    para crear nuestra clase usuario
    """

    def create_user(self, correo_electronico, nombre, password, **other_fields):
        """
        Funcion que crea
        un usuario
        """

        if not correo_electronico:
            raise ValueError("Correo electronico faltante")

        correo_electronico = self.normalize_email(correo_electronico)
        user = self.model(correo_electronico=correo_electronico, nombre=nombre, **other_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, correo_electronico, nombre, password, **other_fields):
        """
        Funcion que crea 
        un superusuario
        """

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        return self.create_user(correo_electronico, nombre, password, **other_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    """
    Definición de la 
    clase usuario
    """

    roles = [
        ('Usuario', 'Usuario'),
        ('Administrador', 'Administrador')
    ]
    id_organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=50)
    correo_electronico = models.EmailField(max_length=50, unique=True)
    rol = models.CharField(choices=roles, default='Usuario', max_length=20)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    password = models.CharField(max_length=50)

    objects = UsuarioManager()

    USERNAME_FIELD = 'correo_electronico'
    REQUIRED_FIELDS = ['nombre']

    def __str__(self):
        return f"{self.nombre}"


class Producto(models.Model):
    """
    Definición de la 
    clase Producto
    """

    nombre = models.CharField(max_length=255)
    categoria = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock_minimo = models.IntegerField(default=5)

    def stock_bajo(self):
        """
        Funcion que verifica si
        el stock es bajo
        """

        return self.cantidad < self.stock_minimo

    def __str__(self):
        return f"{self.nombre}"

class Movimiento(models.Model):
    """
    Definición de la 
    clase Movimiento
    """

    movimientos = [
        ("Salida", "Salida"),
        ("Entrada", "Entrada")
    ]
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE, null=True)
    tipo_movimiento = models.CharField(choices=movimientos, default='Salida', max_length=20)
    cantidad = models.IntegerField()
    fecha = models.DateField(auto_now_add=True)
    descripcion = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.descripcion}"

class Precios(models.Model):
    """
    Definición de la 
    clase Precios
    """

    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.id_producto.nombre} - {self.precio} - {self.fecha}"
