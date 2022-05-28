# django-logistic
## Aplicación de control y visualización de vehiculos, rutas y destinos

Programa demo que resuelve el challenge:

# Administrador de flota
Se desea conocer la ubicación de una flota de vehículos en 3 ciudades distintas.

Para ello se plantea realizar una aplicación donde se pueda visualizar una pantalla donde se vean las ciudades en cuestión y los vehículos que se encuentran en ellas.

A la par, se plantea tener una api rest en la aplicación donde se pueden administrar los vehículos. De esta manera:
- Se puede crear, editar o eliminar los vehículos de la flota.
- Se puede listar los vehículos y su estado actual
- Se puede dar la instrucción de que un vehículo viaje a una ciudad determinada

Un vehículo tiene la siguiente información
- ID de Vehículo
- Ubicación actual
- Consumo de combustible (km/lt)
- Distancia recorrida
- Combustible consumido

Las ciudades tienen la siguiente distancia entre sí:

                   Ciudad A, Ciudad B,  Ciudad C
Ciudad A                 0 ,         1    ,       2
Ciudad B                    ,         0    ,       4
Ciudad C                    ,               ,       0

Al dar la instrucción de que un vehículo viaje a una ciudad se debe de actualizar su información. En particular sus atributos de distancia recorrida y combustible consumido.

### pasos para instalación:

I. Instalar Python

Instale python descargandolo desde su página oficial (version 3.9 o superior)
https://www.python.org/download/

II. Crear un ambiente virtual

Instale el paquete de python virutalenv de la siguiente manera:

> pip install virtualenv

Creamos un ambiente virtual afuera de la carpeta "logistic", con el siguiente comando:

> python -m virtualenv venv

Creada la carpeta nos direccionamos a la carpeta scripts de venv

> cd venv/scripts

Activamos el ambiente virtual con el comando:

> ./activate

Ahora nos posicionamos dentro de la carpeta del proyecto en la carpeta "logistic" y ubicamos el
archivo requirements.txt e instalamos las dependencias necesarias para el proyecto usando el comando:

> pip install -r requirements.txt

III. Levantamiento del proyecto

dentro le la ruta "/logistic/", ubicando el archivo manage.py y teniendo instaladas las dependencias del 
punto II, correremos el proyecto en modo desarrollo, por lo que este paquete ya incluye una base de datos
local en sqlite con datos iniciales, por lo que no es necesario realizar ninguna migración, con base en esto,
aplicamos el comando:

> python manage.py runserver 0.0.0.0:8000

Esto iniciara el proyecto en modo desarrollo.

IV. Ruta aplicación web

Para ingresar en la aplicacion logistic, usando un web browser, ir a la ruta:

> http://localhost:8000/

V. Ruta y documentacion API



