from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class Organizacion(models.Model):
    nombre_organizacion = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Organización"
        verbose_name_plural = "Organizaciones"

    def __str__(self):
        return self.nombre_organizacion

class UsuarioManager(BaseUserManager):

    def create_user(self, correo_electronico, nombre, password, **other_fields):

        if not correo_electronico:
            raise ValueError("Correo electronico faltante")
        
        correo_electronico = self.normalize_email(correo_electronico)
        user = self.model(correo_electronico=correo_electronico, nombre=nombre, **other_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, correo_electronico, nombre, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        return self.create_user(correo_electronico, nombre, password, **other_fields)
    
class Usuario(AbstractBaseUser, PermissionsMixin):
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
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    precio_unidad = models.DecimalField(max_digits=10, decimal_places=2)
    stock_minimo = models.IntegerField()
    id_organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
class Movimiento(models.Model):
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
        return self.descripcion
