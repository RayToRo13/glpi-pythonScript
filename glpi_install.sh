#!/bin/bash
sudo su
cd /var/www/html/glpi
#Commande pour installer glpi automatiquement/
php bin/console db:install -f -n -L fr_FR -H localhost -d glpidb -u glpi -p password
#hostname = localhost, database = glpidb, user = glpi, password = password
#Modifer aux besoins