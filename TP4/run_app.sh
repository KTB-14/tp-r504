#!/bin/bash
# On lance le conteneur Flask
docker run -d \
  --name tp4-app \
  --network net-tp4 \
  -p 5000:5000 \
  -v $(pwd)/srv:/srv \
  im2-tp4

  #-v option mountbind de docker  
  # repertoire de ma machine hote $(pwd)/srv
  # vers le repertoire /srv du conteneur
  # et on change aussi vers im2-tp4
