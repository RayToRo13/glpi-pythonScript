#!/bin/bash

DB="glpidb"
USER="glpi"
PASS="password"

sudo mysql -e "CREATE DATABASE $DB CHARACTER SET utf8 COLLATE utf8_general_ci";
sudo mysql -e "CREATE USER $USER@'127.0.0.1' IDENTIFIED BY '$PASS'";
sudo mysql -e "GRANT SELECT, INSERT, UPDATE ON $DB.* TO '$USER'@'localhost'";
