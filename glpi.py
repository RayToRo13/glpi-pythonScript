#!/usr/bin/env python3
import os
import sys
import paramiko
import yaml

#Simplification des paramètres de connexion
ip = sys.argv[1]
user_name = sys.argv[2]
passwd = sys.argv[3]
log = "ip, user_name, passwd, " 

#fonction de lecture du fichier yaml défini en 4ème argument
def yaml_paquets():
  #lis le fichier package.yml
  import yaml
  fichier = sys.argv[4]
  try :
        #La liste est mise sous un format permettant sa lecture en tant que chaîne,
        #et non plus une liste dans un dictionnaire.
        #Afin que les commandes soient bien interprétée par la fonction ssh.
        with open(fichier) as p:
            paquets = yaml.safe_load(p)
            return paquets
            variable = yaml_paquets()
            var = ' '.join(variable["packages"]["exec"])
            return var
  except :
      print ("Fichier yaml inexistant, vérifier son nom")
      exit()
      
#fonction de connection ssh        
def ssh(log, myCommand):
    
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try :
        s.connect(hostname=ip, username=user_name, password=passwd)
        #La connexion se coupe dès que la commande est terminée.
        stdin, stdout, stderr = s.exec_command('{}'.format(myCommand))
        exit_status = stdout.channel.recv_exit_status()
        return exit_status
        if exit_status == 1:
            print("Erreur", exit_status)  
            print(stdout) 
    
        s.close()
#En cas d'erreur de connexion, log, ou de fonctionnement affichage de l'erreur.
    except :
        e = sys.exc_info()
        print(e)
        print ("Erreur de connexion...")
        time.sleep(1)
        print ("Veuillez vérifier vos paramètres...")
        time.sleep(1)
        exit()            
        
##################################VARIABLES################################  
#Simplication des variables pour les différents appels de celles-ci          
Vars = yaml_paquets()
user = sys.argv[2]
update = "sudo apt-get update -y && sudo apt-get upgrade -y"

#Reboot apache2
com1 = ' '.join(Vars["cmd"]["commande"])
RebootApache = '{}'.format(com1)

#Droits pour v/var/www/html
com2 = ' '.join(Vars["cmd"]["commande2"])
DroitsGLPI = '{}'.format(com2)

#Changement Groupe www-data pour le dossier /var/www/html
com3 = ' '.join(Vars["cmd"]["commande3"])
ChGrpGLPI = '{}'.format(com3)

##########################FIN_VARIABLES############################


#########################DEBUT_SCRIPT################################
print("Mise à jour du système client..\n")
   
ssh(log, update)

print ("Installation des paquets:\n")

#Boucle qui execute une commande tant que des itérations se trouve dans sa liste dans le fichier package.yml     
for key, data in (Vars['packages'].items()):
        pack= ' '.join(data)
        myCommand = "sudo apt-get install "+ pack+ " -y"
        print(pack)
        ssh(log, myCommand)

#Lien vers la dernière version de glpi|Modifier si nécessaire.
ssh(log, 'sudo wget -P /var/tmp https://github.com/glpi-project/glpi/releases/download/9.4.5/glpi-9.4.5.tgz')
print("Téléchargement de GLPI..")

#Extraction du .tgz vers le dossier apache
ssh(log, 'sudo tar xvzf /var/tmp/glpi-9.4.5.tgz -C /var/www/html')

#Restart de apache pour prise en compte du dossier glpi, puis modification des droits de celui ci
ssh(log, RebootApache)
ssh(log, ChGrpGLPI)
ssh(log, DroitsGLPI)

#Application du script mariadb.sh qui crée la base de donnée, avec mot de passe
os.system('ssh {}@192.168.1.58 bash < ./mariadb.sh'.format(user))
print("Transfert du fichier de conf apache2")
ssh(log, 'sudo rm /etc/php/7.3/apache2/php.ini')
####################################################################################

#remplacement du fichier /etc/php/7.3/apache2/php.ini avec une valeur default_socket_timeout = 60 au lieu de 30, pour résoudre
#l'erreur PHP : default_socket_timeout.
#Si version php différente modifier la version de php dans le chemin scp.
os.system('scp php.ini {}@192.168.1.58:/home/{}'.format(user, user))
ssh(log, 'sudo mv /home/{}/php.ini /etc/php/7.3/apache2/'.format(user))
#####################################################################################

ssh(log, RebootApache)

#Connection à la DB glpi automatisé. Instructions dans glpi_install.sh si besoin de modifer les accès, nom de DB.
#Doit être similaire aux logs/db de mariadb.sh
print("Configuration silencieuse de GLPI..")
os.system('ssh {}@192.168.1.58 bash < ./glpi_install.sh'.format(user))
######################################################################################

#Suppression du fichier install.php (pour sécurité) et du glpi-x.x.x.tgz
ssh(log, 'sudo rm /var/www/html/glpi/install/install.php')
ssh(log, 'sudo rm /var/tmp/glpi-9.4.5.tgz'.format(user))
ssh(log, RebootApache)
print("Deconnexion du serveur..")
######################################################################################
