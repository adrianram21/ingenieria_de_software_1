from django.db import models

# Modelo de prueba para verificar la conexion entre el back y el front

class Prueba(models.Model):
    texto = models.CharField(max_length=30)

    def __str__(self):
        return self.texto
    
