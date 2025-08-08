# Utiliser une image Python officielle
FROM python:3.10-slim-buster

# Empêcher Python de mettre en mémoire tampon les sorties stdout et stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Installer les dépendances
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code de l'application
COPY . /app/