# 1. Choisir une image Python légère
FROM python:3.10-slim

# 2. Installer FFmpeg
RUN apt-get update && apt-get install -y ffmpeg

# 3. Créer un dossier de travail
WORKDIR /app

# 4. Copier les fichiers du projet
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 5. Exposer le port (Render utilisera la variable PORT)
EXPOSE 8080

# 6. Lancer l'app avec gunicorn sur le port 8080
CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:8080"]
