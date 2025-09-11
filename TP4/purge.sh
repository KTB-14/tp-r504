#!/bin/bash

# Ecrire un script purge.sh qui va arreter et supprimer tous les conteneurs, qu’ils soient lancés ou arretés.

# docker ps -aq 
# montre tous les conteneurs, que leur id ( ceux en cours et arrêtés)

# docker stop nom_id
# arrete les conteneurs en cours

#supprimer les conteneurs
docker stop $(docker ps -aq)

docker rm $(docker ps -aq)


# si besoin supprimer tous inclus les images : docker system prune -af --volumes 
docker system prune -f --volumes 