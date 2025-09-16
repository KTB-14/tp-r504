#!/bin/bash

# Si le conteneur tourne, on l'arrête
docker stop tp4-app 2>/dev/null || true

# On supprime le conteneur (même arrêté)
docker rm tp4-app 2>/dev/null || true

# Lancement du conteneur Flask
docker run -d \
  --name tp4-app \
  --network net-tp4 \
  -p 5000:5000 \
  -v "$(pwd)/srv:/srv" \
  im2-tp4

# -v option bind mount :
#   répertoire de la machine hôte $(pwd)/srv
#   monté dans /srv du conteneur
# image utilisée : im2-tp4
