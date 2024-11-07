# Biblioteca

Este es un proyecto Django para gestionar una biblioteca.

## Instalación

1. Clona el repositorio:
    ```sh
    git clone <URL_DEL_REPOSITORIO>
    ```

2. Navega al directorio del proyecto:
    ```sh
    cd biblioteca
    ```

3. Activa el entorno virtual:
    ```sh
    source biblioteca_env/Scripts/activate
    ```

4. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

1. Aplica las migraciones:
    ```sh
    python manage.py migrate
    ```

2. Ejecuta el servidor de desarrollo:
    ```sh
    python manage.py runserver
    ```

3. Abre tu navegador y navega a `http://127.0.0.1:8000/` para ver la aplicación en funcionamiento.

## Estructura de la Aplicación

- `biblioteca/`: Contiene la configuración principal del proyecto.
  - `settings.py`: Configuración del proyecto.
  - `urls.py`: Definición de las rutas principales.
  - `wsgi.py`: Configuración para el servidor WSGI.
  - `asgi.py`: Configuración para el servidor ASGI.

- `catalogo/`: Contiene la aplicación principal de la biblioteca.
  - `models.py`: Definición de los modelos de datos.
  - `views.py`: Definición de las vistas.
  - `urls.py`: Definición de las rutas de la aplicación.
  - `admin.py`: Configuración del panel de administración.
  - `tests.py`: Pruebas unitarias de la aplicación.

## Contribuir

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Sube tus cambios a tu fork (`git push origin feature/nueva-funcionalidad`).
5. Crea un nuevo Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.