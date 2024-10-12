# Utiliser une image de base avec Python
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /usr/src/app

# Copier tout le contenu du dossier app dans le répertoire de travail
COPY app/ .

# Installer les dépendances à partir de requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exposer un port (si l'application en a besoin)
EXPOSE 8000

# Lancer le script Python
CMD ["python", "server.py"]