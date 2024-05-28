# Usamos la última versión de Python
FROM python:3.7

# Copiamos los archivos de nuestra aplicación al contenedor
COPY . /app

# Cambiamos el directorio de trabajo
WORKDIR /app

# Instalamos venv y creamos el entorno virtual
RUN python -m venv venv

# Activamos el entorno virtual y luego instalamos las dependencias
RUN . venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

# Configuramos el entorno virtual para que se utilice por defecto
ENV PATH="/app/venv/bin:$PATH"

# Ejecutamos nuestra aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
