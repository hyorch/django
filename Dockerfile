FROM python:3.10.4-slim-bullseye

# Set Python environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de Trabajo
WORKDIR /code

# Instalar dependencias del sistema
COPY ./requirements.txt .

# Instalar dependencias de Python
RUN pip install -r requirements.txt

# Copiar Proyecto
COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
# Exponer el puerto 8080
EXPOSE 8080




