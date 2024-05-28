# Usamos la última versión de Python
FROM python:latest

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos solo los archivos de requerimientos primero para aprovechar la caché de Docker
COPY requirements.txt .

# Instalamos venv y creamos el entorno virtual
RUN python -m venv venv

# Actualizamos pip e instalamos las dependencias
RUN . venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

# Copiamos el resto de los archivos de nuestra aplicación al contenedor
COPY . .

# Configuramos el entorno virtual para que se utilice por defecto
ENV PATH="/app/venv/bin:$PATH"

# Exponemos el puerto que Uvicorn usará
EXPOSE 8000

# Ejecutamos nuestra aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
