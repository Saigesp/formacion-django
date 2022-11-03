# prueba django

# INSTALACIÓN

# 1. para instalar django, primero tengo que instalar un entorno virtual (evita conflictos de versiones): python3 -m venv .
# 2. Este entorno virtual lo tengo que activar: source bin/activate
# 3. (prueba-django) patricia@MacBook-Pro-de-Patricia prueba-django % En la terminal aparece ya el entorno virtual. Todos los paquetes se guardarán en las carpetas lib e include
# 4. Instalo Django: python -m pip install Django
# 5. Compruebo que está instalado y la versión: python -m django --version (python -m indica que selecciones el modulo X, en este caso django)
# 6. Empiezo el proyecto de django, y lo llamo backend: django-admin startproject backend
# 7. Para levantar el proyecto, uso este comando: python backend/manage.py runserver
# 8. Migraciones son necesarias cuando se modifica la base de datos ( edición, creación de modelos ) Son instrucciones para hacer esos cambios en la base de datos: python backend/manage.py migrate
# 9. Crear archivo .gitignore en la raíz del proyecto: Para no subir al repositorio archivos que no son necesarios registrar sus cambios porque no van a sufrir cambios y porque son propios de mi ordenador
# 10. Crear administrador. Registrar un primer usuario para la tabla o aplicación de auth, con permisos de admin: python backend/manage.py createsuperuser
# 11. username: admin, email: admin@gmail.com, password:admin

# ESTRUCTURA Y VISTAS

# 1. En django el proyecto se organiza en apps (carpetas) que por lo general se organizan por funcionalidad
# 2. para crear una app llamada articles usar este comando: python backend/manage.py startapp articles
    # 2.1 Dentro de esta app, el archivo models.py donde tengo los modelos, si estos modelos quiero mostrarlos en el admin para poder editarlos desde allí, tengo que crearlos también en el archivo admin.py

