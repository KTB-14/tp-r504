#!/bin/bash

# lancement serveur sql
docker run --rm -d \
--name tp4-sql \
--network net-tp4 \
--env MYSQL_ROOT_PASSWORD=foo \
-p 3307:3306 \
-v vol-sql-tp4:/var/lib/mysql \
mysql:8.0

