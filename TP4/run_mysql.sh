#!/bin/bash

# lancement serveur sql
if docker inspect tp4-sql >/dev/null 2>&1; then
    docker start tp4-sql >/dev/null 2>&1
else
    docker run -d \
        --name tp4-sql \
        --network net-tp4 \
        --env MYSQL_ROOT_PASSWORD=foo \
        -p 3307:3306 \
        -v vol-sql-tp4:/var/lib/mysql \
        mysql:8.0
fi
