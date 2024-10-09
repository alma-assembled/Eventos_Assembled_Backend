# Usa la imagen base oficial de Python
FROM python:3.11.4

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo requirements.txt al contenedor de trabajo
COPY requirements.txt requirements.txt

# Establece las variables de entorno para Flask
ENV FLASK_APP=index.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN pip install --upgrade pip

# Copia el archivo .env al contenedor
COPY .env /app/.env

# Instala las dependencias
RUN pip install -r requirements.txt

# Verifica las variables de entorno (opcional, solo para depuración)
RUN cat /app/.env

# Copia todos los archivos del proyecto al contenedor de trabajo
COPY . .

# Define el comando por defecto para ejecutar la aplicación
CMD ["python", "index.py"]
