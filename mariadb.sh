#!/bin/bash

sudo mysql -e "CREATE DATABASE glpidb";
sudo mysql -e "CREATE USER 'glpi'@'localhost' IDENTIFIED BY 'password'";
sudo mysql -e "GRANT ALL ON glpidb.* TO 'glpi'@'localhost'";
sudo mysql -e "FLUSH PRIVILEGES";
