#!/bin/sh
# Espera hasta que PostgreSQL esté listo
until nc -z db 5432; do
  echo "Esperando a que PostgreSQL esté listo..."
  sleep 1
done

# Levanta FastAPI
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
