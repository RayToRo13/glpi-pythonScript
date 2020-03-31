# glpi-pythonScript
Pré requis:

Yaml python
Pip
Paramiko

Script d'installation glpi sous python

Script permettant l'installation de glpi sur une machine distante. 
Utilise le protocole ssh(paramiko). 

Pour lancer le script il faut 4 arguments :
glpi.py #ip #user_ssh #pass_user_ssh #package.yaml à utiliser. 


Les infos de la base de donnée se modifient dans mariadb.sh.
Répercuter les modifications dans glpi.sh
