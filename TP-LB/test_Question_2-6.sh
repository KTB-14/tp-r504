#!/bin/bash

reponse1=0
reponse2=0

for ((i=0;i<500;i++)); do
  a=$(curl -s localhost:83)
  if echo "$a" | grep "Hello 1"; then
    reponse1=$((reponse1+1))
  elif echo "$a" | grep "Hello 2"; then
    reponse2=$((reponse2+1))
  fi
done

echo "Nombre TOTAL de Hello 1 : $reponse1"
echo "Nombre TOTAL de Hello 2 : $reponse2"
