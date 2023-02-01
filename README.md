# Formación Django

**importante** python se escribe con snakecase

## Trabajar con django

1. Activar entorno virtual (Hay que hacerlo siempre para levantar el proyecto):

```sh
source .env/bin/activate
# puede estar en otro sitio, como .venv/bin/activate
# o env/bin/activate, por ejemplo
```

2. Comprobar que en la terminal aparece ya el entorno virtual:
```sh
patricia@MacBook prueba-django %                # <- en mac
(prueba-django) patricia@MacBook: $             # <- en linux
```

3. Con el entorno activado, ejecutar las migraciones (instrucciones para hacer cambios en la base de datos). Son necesarias siempre que se modifica la base de datos (edición, creación de modelos, etc):
```sh
python backend/manage.py migrate
```

4. Con el entorno activado, levanto el proyecto:
```sh
python backend/manage.py runserver
```

## Empezar un nuevo proyecto

1. Primero instalar un entorno virtual (evita conflictos de versiones) en la carpeta "**.env**":
```sh
python3 -m venv .env/
```

2. Activar el entorno virtual:
```sh
source .env/bin/activate
```
> En la terminal aparece ya el entorno virtual: `patricia@MacBook-Pro-de-Patricia prueba-django %`

3. Instalo Django
```sh
python -m pip install Django
```

4. Compruebo que está instalado viendo la versión

```sh
python -m django --version
```
> `python -m` indica que selecciones el modulo X, en este caso Django

5. Con el entorno activado, creo archivos de django, llamando al proyecto "**backend**":
```sh
django-admin startproject backend
```

6. Ejecuto las migraciones:
```sh
python backend/manage.py migrate
```

7. Creo un administrador (un primer usuario con permisos de admin):
```sh
python backend/manage.py createsuperuser
# username: admin, email: admin@gmail.com, password:admin
```

## Estructura y vistas

En django el proyecto se organiza en apps (carpetas) que por lo general se organizan por funcionalidad (artículos, compras, etc).

1. Para crear una app llamada articles usar este comando:
```sh
python backend/manage.py startapp articles
```

2. Una vez tengo la app, tengo que añadirla en el fichero de `settings.py` en la variable `INSTALLED_APPS`.

### Parámetros para llamar a los endpoints

- queryparams (son opcionales, caso más habitual: filtros)
- parametros dentro de la url (son necesarios para la función definida)
- parametros que envío con un post en el body (se usan cuando son más complejos, enviar json etc)

## Modelos

Son los archivos que reflejan la estructura de la base de datos

### Cada modelo en su propio archivo
- Si en lugar de tener solo un archivo `models.py` quiero tener una carpeta para organizar modelos, creo una carpeta llamada `models` y dentro un archivo `__init__.py` (este archivo indica que esta carpeta es un módulo, y que por tanto voy a poder importar funciones de archivos en esa carpeta)

### Ver los modelos en el admin de django
- Dentro de su app, si quiero mostrarl en el admin un modelo para poder editarlo desde allí, tengo que registrarlos en el archivo `admin.py`:

```python
from django.contrib import admin
from .models import Article # importar modelo que vas a registrar

admin.site.register(Article) # Registro simple
```

## Migraciones

[Documentación de Django](https://docs.djangoproject.com/en/4.1/topics/migrations/)

1. Cuando creo, elimino o modifico un modelo, hay que generar las migraciones (instrucciones da cambio para la base de datos). Para ello ejecuto el comando:
```sh
python backend/manage.py makemigrations
```

2. Una vez se han generado, ejecuto las migraciones con el comando:
```sh
python backend/manage.py migrate
```

### Migraciones custom (manuales)

```python
from django.db import migrations

def apply_migration(apps, *args):
    ModeloAMigrar = apps.get_model("app_donde_esta_el_modelo", "ModeloAMigrar")
    # hacer cosas con el modelo

def revert_migration(apps, *args):
    ModeloAMigrar = apps.get_model("app_donde_esta_el_modelo", "ModeloAMigrar")
    # deshacer cosas con el modelo

class Migration(migrations.Migration):

    dependencies = [
        ("app_1", "0004_nombre_migracion_previa"), # <- migraciones previas necesarias
        ("app_2", "0025_nombre_migracion_previa"), # <- migraciones previas necesarias
    ]

    operations = [
        migrations.RunPython(apply_migration, revert_migration)
    ]
```

## Testing

[Documentación de django](https://docs.djangoproject.com/en/4.1/topics/testing/overview/).

Django utiliza el módulo [unittest](https://docs.python.org/3/library/unittest.html)

## Django Rest Framework

[Documentación de DRF](https://www.django-rest-framework.org/)

### API Rest

- Cada modelo tiene su propio endpoint: `api/comments/`, `api/articles/`, etc...
- Métodos CRUD - Create, Read, Update, Delete:
    - Create:
        - POST al endpoint: `api/comments/`   
        - método `create()` en un viewset
    - Read (all):
        - GET al endpoint: `api/comments/` 
        - método `list()` en un viewset
    - Read (filter):
        - GET al endpoint: `api/comments/?{parameter1}={param1-value}&{parameter2}={param2-value}` 
        - método `list()` en un viewset
    - Read (one):
        - GET al endpoint: `api/comments/{comment-id}/` 
        - método .retrieve() en un viewset
    - Update (all fields):
        - PUT al endpoint: `api/comments/{comment-id}` (hay que pasarle datos) 
        - método `update()` en un viewset
    - Update (some fields):
        - PATCH al endpoint: `api/comments/{comment-id}` (hay que pasarle datos) 
        - método `partial_update()` en un viewset
    - Delete:
        - DELETE al endpoint: `api/comments/{comment-id}/` 
        - método `destroy()` en un viewset
