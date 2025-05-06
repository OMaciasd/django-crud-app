#!/bin/bash

# Salir si hay errores
set -e

# Crear el archivo .env con las variables necesarias
cat <<EOF > .env
DB_USER=${DB_USER}
DB_PASSWORD=${DB_PASSWORD}
SECRET_KEY=${SECRET_KEY}
DEBUG=True
EOF

echo ".env generado exitosamente:"
cat .env

# Ejecutar las migraciones y levantar el servidor (puedes ajustarlo según tus necesidades)
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
