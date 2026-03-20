# Proyecto FastAPI + PostgreSQL con Docker

Este proyecto es una aplicación **FastAPI** conectada a una base de datos **PostgreSQL**, completamente **contenedorizada con Docker**.  
El objetivo es demostrar cómo construir, conectar y ejecutar un entorno backend moderno con una arquitectura limpia y fácilmente replicable.

---

## Descripción

Este proyecto implementa operaciones **CRUD (Create, Read, Update, Delete)** sobre una base de datos PostgreSQL, utilizando:

- **FastAPI** como framework backend.
- **SQLAlchemy** como ORM (Object Relational Mapper).
- **Pydantic** para validación de datos.
- **Docker y Docker Compose** para gestionar los contenedores.

Con esta estructura, cualquier desarrollador puede levantar el proyecto con un solo comando, sin necesidad de configurar manualmente entornos o dependencias locales.

---

## Estructura del proyecto

docker_proyecto01/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── entrypoint.sh
├── main.py
├── database.py
├── models.py
├── schemas.py
├── routers/
│ └── posts.py
└── README.md


**Descripción breve de los archivos principales:**

- `Dockerfile`: define cómo se construye la imagen del contenedor web (FastAPI).
- `docker-compose.yml`: orquesta los contenedores (web y base de datos).
- `requirements.txt`: contiene las dependencias de Python necesarias.
- `entrypoint.sh`: script que espera a que la base de datos esté lista antes de iniciar el servidor.
- `main.py`: punto de entrada de la aplicación.
- `database.py`, `models.py`, `schemas.py`: configuración, modelos y validación de datos.
- `routers/posts.py`: contiene las rutas para las operaciones CRUD.

---

## Requisitos previos

Antes de comenzar, asegúrate de tener instalados los siguientes programas:

- **Python 3.9+**
- **Docker Desktop** (o Docker Engine + Docker Compose)
- **Git** (para clonar el repositorio)
- **Visual Studio Code** (opcional pero recomendado)

---

## Cómo ejecutar el proyecto

Sigue estos pasos para ejecutar el proyecto en tu máquina:

### 1️ Clonar el repositorio

Abre tu terminal o Git Bash y ejecuta:

git clone https://github.com/JERO2016/Primer_proyecto_fastapi_docker.git

### 2 Entrar al directorio del proyecto

cd Primer_proyecto_fastapi_docker

### 3️ Construir y levantar los contenedores

Ejecuta el siguiente comando para construir y ejecutar todo el entorno:

docker compose up --build -d

Esto hará lo siguiente:

Construirá la imagen del contenedor FastAPI.
Creará y levantará el contenedor de PostgreSQL.
Levantará el servidor web disponible en el puerto 8000.

### 4️ Acceder a la aplicación

Abre tu navegador y visita:

👉 http://localhost:8000

Si ves el mensaje "Hello World" o el contenido de tu API, significa que todo está funcionando correctamente 

### 5️ Acceder a la documentación interactiva

FastAPI incluye una interfaz automática de documentación. Puedes acceder a ella en:

Swagger UI → http://localhost:8000/docs

ReDoc → http://localhost:8000/redoc

### Comandos útiles de Docker

# Ver los contenedores en ejecución
docker ps

# Detener todos los contenedores
docker compose down

# Reconstruir imágenes y reiniciar contenedores
docker compose up --build -d

# Ver los logs del contenedor "web"
docker compose logs -f web

### Notas adicionales

Si modificas el código fuente, los cambios se reflejarán automáticamente gracias al volumen montado.

Si agregas nuevas dependencias en requirements.txt, recuerda reconstruir el contenedor con:

docker compose up --build -d

Los datos de la base de datos se almacenan en un volumen llamado postgres_data.

### Autor

C. Jesús Emmanuel Ramírez Orozco

Proyecto de aprendizaje desarrollado como parte de formación práctica en Data Engineering y desarrollo backend con Python, basado en el artículo
"Dockerizing FastAPI and PostgreSQL: Effortless Containerization — A Step-by-Step Guide"
