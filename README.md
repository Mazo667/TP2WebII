# TP2 PROGRAMACION WEB II
<img src="https://repository-images.githubusercontent.com/853067853/dd71ff3a-6df4-4d84-b537-eff808cba4ec" alt="logo">

[Informe realizado](InformeTP2WEBII.pdf)

# Proyecto Django: Tablero Mensajes

Desarrollar un proyecto Django denominado TableroMensajes siguiendo el patrón de diseño
Modelo-Vista-Plantilla (MVT). Este proyecto permitirá a las/los estudiantes aplicar conceptos
fundamentales de Django, como la creación de vistas basadas en funciones y en clases, el
uso del Django Template Language (DTL), modularización y reutilización de plantillas, y la
implementación de funcionalidades clave como la creación, visualización y eliminación de
mensajes.

## Tabla de Contenidos

- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Informe de Desarrollo](#informe-de-desarrollo)

## Requisitos

- Python 3.12.3 o superior
- Django 5.1 o superior

## Instalación

1. **Clonar el repositorio**:
    ```bash
    git clone https://github.com/Mazo667/TP1Django.git
    ```
2. **Desplazarnos al repositorio creado**:
    ```bash
    cd TP1Django
    ```
3. **Crear un entorno virtual**:
    ```bash
    virtualenv env
    ```
4. **Activar el entorno virtual**:
    ```bash
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```
5. **Instalar los requirimientos**:
    ```bash
    pip install -r requirements.txt
    ```
6. **Aplicar las migraciones**:
    ```bash
    python manage.py migrate
    ```
7. **Crear un superusario(opcional)**:
    ```bash
    python manage.py createsuperuser
    ```
8. **Inicia el servidor**:
    ```bash
    python manage.py runserver
    ```

## Informe de Desarrollo

<h3> 1. Planificación del Proyecto:</h3>
<li>Definición de requisitos y funcionalidades del tablero mensajes</li>
<li>Diseño de la estructura de la base de datos y modelos.</li>
<h3> 2. Configuración del Entorno:</h3>
<li>Instalación de Django y configuración del entorno virtual.</li>
<li>Creación de un repositorio en GitHub.</li>
<h3>3. Desarrollo de Modelos:</h3>
<li>Implementación del modelo Mensaje para almacenar información sobre los mensajes.</li>
<li>Creación de migraciones y aplicación de las mismas para crear las tablas en la base de datos.</li>
<h3>4. Desarrollo de Vistas:</h3>
<li>Implementación de vistas basadas en clase para manejar la creación, visualización y eliminación de mensajes.</li>
<li>Implementación de la lógica de búsqueda para filtrar mensajes por destinatario o remitente.</li>
<h3>5. Desarrollo de Plantillas:</h3>
<li>Creación de plantillas HTML utilizando Bootstrap para un diseño responsivo y moderno.</li>
<li>Implementación de formularios para la creación de mensajes y búsqueda.</li>
<h3>6. Pruebas:</h3>
<li>Realización de pruebas manuales para asegurar que todas las funcionalidades funcionen correctamente.</li>
<li>Corrección de errores y optimización del código.</li>
<h3>Documentación:</h3>
<li>Redacción de este archivo README.md para proporcionar instrucciones claras sobre la instalación, configuración y uso del proyecto.</li>
