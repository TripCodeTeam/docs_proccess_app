# Usamos la última versión de Python
FROM python:latest

# Copiamos los archivos de nuestra aplicación al contenedor
COPY . /app

# Cambiamos el directorio de trabajo
WORKDIR /app

# Instalamos las dependencias
RUN python -m pip install -r requirements.txt

# Ejecutamos nuestra aplicación
CMD ["uvicorn","main:app", "--host", "0.0.0.0","--port", "80"]