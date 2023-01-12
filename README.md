# Formación Django

**importante** python se escribe con snakecase

# INSTALACIÓN

Primero instalar un entorno virtual (evita conflictos de versiones):
```sh
python3 -m venv .env/
```

Este entorno virtual lo tengo que activar:

```sh
source .env/bin/activate
```

En la terminal aparece ya el entorno virtual:

```sh
patricia@MacBook-Pro-de-Patricia prueba-django % 
```
> Hay que hacerlo siempre para levantar el proyecto

Instalo Django

```sh
python -m pip install Django
```

Compruebo que está instalado y la versión

```sh
python -m django --version
```

> `python -m` indica que selecciones el modulo X, en este caso Django

Con el entorno activado, levanto el proyecto, uso este comando

```sh
python backend/manage.py runserver
```

Las migraciones son necesarias cuando se modifica la base de datos (edición, creación de modelos). Son instrucciones para hacer esos cambios en la base de datos

```sh
python backend/manage.py migrate
```

Crear administrador. Registrar un primer usuario para la tabla o aplicación de auth, con permisos de admin

```sh
python backend/manage.py createsuperuser
# username: admin, email: admin@gmail.com, password:admin
```

# EMPEZAR PROYECTO DE NUEVO

COn el entorno activado, crear archivos de django, llamando al proyecto **"backend"**:

```sh
django-admin startproject backend
```

## ESTRUCTURA Y VISTAS

1. En django el proyecto se organiza en apps (carpetas) que por lo general se organizan por funcionalidad.
2. Para crear una app llamada articles usar este comando:
    ```
    python backend/manage.py startapp articles
    ```
3. Una vez tengo la app, tengo que añadirla en el fichero de `settings.py` en la variable `INSTALLED_APPS`

# MODELOS
1. Si en lugar de tener solo un archivo models.py, sino que quiero tener una carpeta para organizar modelos, creo una carpeta llamada models y dentro un archivo `__init__.py`. (este archivo lo que indica es que mi carpeta es un módulo, y que por tanto voy a poder importar y exportar "datos")

2. Una vez creo un modelo, uso comando:
    ```
    python backend/manage.py makemigrations
    ```
    para generar las instrucciones que indican como modificar la base de datos, una vez se han generado, migro la base de datos con el comando migrate

    1. Dentro de esta app, el archivo models.py donde tengo los modelos, si estos modelos quiero mostrarlos en el admin para poder editarlos desde allí, tengo que crearlos también en el archivo admin.py ---> admin.site.register(Article) (article es el nombre del modelo)

# MIGRACIONES

[Documentación de Django](https://docs.djangoproject.com/en/4.1/topics/migrations/)

# Parámetros

- queryparams (son opcionales, caso más habitual: filtros)
- parametros dentro de la url (son necesarios para la función definida)
- parametros que envío con un post en el body (se usan cuando son más complejos, enviar json etc)

