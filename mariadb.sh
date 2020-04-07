#!/bin/bash
#Noms des db, user modifiable, mais modification du script glpi_install.sh à remplir de façon 
#à concorder avec la création de la DB
sudo mysql -e "CREATE DATABASE glpidb";
sudo mysql -e "CREATE USER 'glpi'@'localhost' IDENTIFIED BY 'password'";
sudo mysql -e "GRANT ALL ON glpidb.* TO 'glpi'@'localhost'";
sudo mysql -e "FLUSH PRIVILEGES";