#Test
Pré requis:

Yaml python Pip Paramiko

Script d'installation glpi sous python

Script permettant l'installation de glpi sur une machine distante.
 Utilise le protocole ssh(paramiko).

Pour lancer le script il faut 4 arguments : 
glpi.py #ip #user_ssh #pass_user_ssh #package.yaml à utiliser.

Les infos de la base de donnée se modifient dans mariadb.sh. 
Répercuter les modifications dans glpi_install.sh

Le code des différents script sont commentés.
#test
Le script necessite les droits sudo sans mot de passe, pour l'utilisateur avec lequel on se connecte sur la machine distante.

Sudo sans password :
$user = utilisateur avec lequel on va se connecter et éxécuter le script

éditer le fichier en root:

/etc/sudoers et y ajouter :

$user ALL=(ALL) NOPASSWD: ALL
