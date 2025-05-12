# Usa una imagen base ligera con Python
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de dependencias e instálalas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente
COPY app/ ./app/
COPY app/custom_model.h5 ./app/custom_model.h5

# Expone el punto de entrada del contenedor
ENTRYPOINT ["python", "app/main.py"]
