FROM python:3.9.13

# Créer un répertoire pour l'application
RUN mkdir /app

# Définir /app comme répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires pour l'application
#COPY requirements.txt .
COPY utils .
COPY ressources .
COPY TP.py .
COPY requirements.txt .

# Installer les dépendances
RUN pip install -r requirements.txt

# Exposer le port sur lequel l'application écoute
EXPOSE 5000

# Définir les variables d'environnement pour l'application
ENV FLASK_APP=TP.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Lancer l'application
CMD ["flask", "run"]