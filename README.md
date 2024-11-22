## ingenieria_de_software_1
Repositorio para el desarrollo del proyecto de la materia Ingeniería de Software 1

En este repositorio se creara un gestor de inventarios el cual contara tanto con el codigo del proyecto asi como con la documentacion necesaria para formular correctamente el desarrollo de este software. 

Para la realizacion del proyecto se usara Vuejs para el frontend y django REST para el backend. Tambien sera necesario tener instalado nodejs para poder hacer uso del manejador de paquetes npm.

# Ejecucion del proyecto

## Ejecucion del backend 

Para ejecutar el backend es necesario descargar e instalar python (link: https://www.python.org/). Una vez instalado python hay que ir a ingenieria_de_software_1\Proyecto y activar el entorno virtual usando el siguiente comando en la terminal:  

.\venv\Scripts\activate  

Despues de activar el entorno virtual, hay que ir a ingenieria_de_software_1\Proyecto\backend_djangoREST y ejecutar el siguiente comando en la terminal:

pip install -r instalaciones.txt  

Por ultimo, se ejecuta el siguiente comando en la terminal:

python manage.py runserver  

Con este ultimo comando se ejecutara el backend del proyecto y nos dara un link para acceder a este

## Ejecucion del frontend

Para ejecutar el frontend del proyecto es necesario descargar nodejs (link: https://nodejs.org/en/) y realizar la instalacion recomendada. Una vez instalado nodejs, hay que dirigirse a ingenieria_de_software_1\Proyecto\frontend_vuejs y ejecutar el siguiente comando desde la terminal: 

npm run serve  

Esto desplegara el proyecto y nos dara el link para acceder
