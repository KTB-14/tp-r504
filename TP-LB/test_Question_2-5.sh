#!/bin/bash

for ((i=0;i<500;i++)); do 
  a=$(curl -s localhost:83)
  echo $a
done
