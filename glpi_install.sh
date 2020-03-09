#!/bin/bash
sudo su
cd /var/www/html/glpi
#Commande pour installer glpi automatiquement/Se placer dans /var/www/html/glpi en root pour effectuer la commande
php bin/console db:install -f -n -L fr_FR -H localhost -d glpidb -u glpi -p password