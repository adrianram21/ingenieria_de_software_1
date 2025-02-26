"""
Tests de la aplicación
inventario
"""

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from inventario.models import Usuario, Organizacion

class TestLogin(APITestCase):
    
    def setUp(self):

        self.loginURL = '/inventario/login'
        self.client = APIClient()

        self.datosAdministrador = {
            "nombre": "Jaime",
            "rol": "Administrador",
            "organizacion": "Organizacion1",
            "correo_electronico": "jaime@example.com",
            "password": "123456789"
        }

        self.datosUsuario = {
            "nombre": "Juan",
            "rol": "Usuario",
            "organizacion": "Organizacion1",
            "correo_electronico": "Juan@example.com",
            "password": "123456789"
        }

        self.nombreOrganizacion = "Organizacion1"

        self.organizacion = Organizacion.objects.create(nombre_organizacion=self.nombreOrganizacion)

        self.administrador = Usuario.objects.create_user(
            nombre=self.datosAdministrador['nombre'],
            rol=self.datosAdministrador['rol'],
            id_organizacion=self.organizacion,
            correo_electronico=self.datosAdministrador['correo_electronico'],
            password=self.datosAdministrador['password']
        )
        
        self.usuario = Usuario.objects.create_user(
            nombre=self.datosUsuario['nombre'],
            rol=self.datosUsuario['rol'],
            id_organizacion=self.organizacion,
            correo_electronico=self.datosUsuario['correo_electronico'],
            password=self.datosUsuario['password']
        )

    def test_login_correcto_administrador(self):

        response = self.client.post(self.loginURL,
                                    {
                                        "correo_electronico": self.datosAdministrador['correo_electronico'],
                                        "password": self.datosAdministrador['password'] 
                                    },
                                    format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

    def test_login_correcto_usuario(self):

        response = self.client.post(self.loginURL,
                                    {
                                        "correo_electronico": self.datosUsuario['correo_electronico'],
                                        "password": self.datosUsuario['password'] 
                                    },
                                    format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_login_incorrecto_administrador(self):

        response = self.client.post(self.loginURL,
                                    {
                                        "correo_electronico": self.datosAdministrador['correo_electronico'],
                                        "password": "passwordIncorrecta" 
                                    },
                                    format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_incorrecto_usuario(self):

        response = self.client.post(self.loginURL,
                                    {
                                        "correo_electronico": self.datosUsuario['correo_electronico'],
                                        "password": "passwordIncorrecta"  
                                    },
                                    format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
