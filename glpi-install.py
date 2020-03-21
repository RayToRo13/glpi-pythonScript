#!/usr/bin/env python3
import os
import sys
import paramiko
import time
import yaml

#Simplification des paramètres de connexion
ip = sys.argv[1]
user_name = sys.argv[2]
passwd = sys.argv[3]
log = "ip, user_name, passwd, " 

#Connexion au serveur sous le format glpi-install.py IP USERNAME PASSWORD /chemin du fichier yaml/fichier.yml
#L'appel de la def à besoin du/des packages que l'on souhaite installer, ils sont dans le fichier package.yml

def ssh(log, myCommand):
    
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try :
        s.connect(hostname=ip, username=user_name, password=passwd)
        s.exec_command('{}'.format(myCommand))
        time.sleep(13)
        s.close()
    except :
        print ("Erreur de connexion...")
        time.sleep(1)
        print ("Veuillez vérifier vos paramètres...")
        time.sleep(1)
        exit()            
        

def yaml():
#lis le fichier package.yml
  import yaml
  fichier = sys.argv[4]
  try :
        with open(fichier) as p:
            paquets = yaml.safe_load(p)
            return paquets
            variable = yaml()
            var = ' '.join(variable["packages"]["exec"])
#lecture des valeurs de la liste "exec" sous forme de string sans caractères spéciaux.
            print(var)
  except :
      print ("Fichier yaml inexistant, vérifier son nom")
      exit()
                    
##################################VARIABLES################################
Vars = yaml()

#Déclaration de mes variables pour simplification
#Lecture des listes dans le dictionnaire yaml
php = ' '.join(Vars["packages"]["php1"])
PaquetsPhp = 'sudo apt-get install {} -y'.format(php)


apache2 = ' '.join(Vars["packages"]["exec"])
maCommand = 'sudo apt-get install {} -y'.format(apache2)

mariadb = ' '.join(Vars["packages"]["exec2"])
PaquetMariaDB = 'sudo apt-get install {} -y'.format(mariadb)

#Reboot apache2
com1 = ' '.join(Vars["packages"]["commande"])
RebootApache = '{}'.format(com1)

#Droits pour v/var/www/html
com2 = ' '.join(Vars["packages"]["commande2"])
DroitsGLPI = '{}'.format(com2)

#Changement Groupe www-data pour le dossier /var/www/html
com3 = ' '.join(Vars["packages"]["commande3"])
ChGrpGLPI = '{}'.format(com3)

#Mise à jour paquets
com4 = ' '.join(Vars["packages"]["commande4"])
update = '{}'.format(com4)

##########################FIN_VARIABLES############################


#########################DEBUT_SCRIPT################################
#Lien vers la dernière version de glpi|Modifier si nécessaire.
user = sys.argv[2]
print("Connexion en cours...")   
ssh(log, 'sudo wget -P /var/tmp https://github.com/glpi-project/glpi/releases/download/9.4.5/glpi-9.4.5.tgz')
print("Téléchargement de GLPI..")
time.sleep(20)

print("Mise à jour du système")
time.sleep(10)

ssh(log, update)
time.sleep(40)
print("...........5%")
print("Installation des modules LAMP")
ssh(log, RebootApache)
time.sleep(10)

print("...........10%")
print("installation des modules php..")
#Re-installation des modules pour valider les intallations
ssh(log, PaquetMariaDB)
time.sleep(45)
ssh(log, RebootApache)
time.sleep(10)
print("...........25%")
print("Redémarrage du service MariaDB")
ssh(log, PaquetsPhp)
time.sleep(10)

print("...........35%")
ssh(log, ChGrpGLPI)
print("...........50%")
ssh(log, RebootApache)
print ("Redémarrage de apache2")
time.sleep(10)

ssh(log, 'sudo tar xvzf /var/tmp/glpi-9.4.5.tgz -C /var/www/html')
time.sleep(20)

print("...........60%")
ssh(log, RebootApache)
print("Configuration finale de GLPI")
print("...........70%")
ssh(log, PaquetsPhp)
ssh(log, DroitsGLPI)
ssh(log, ChGrpGLPI)
print("...........85%")
ssh(log, RebootApache)
time.sleep(10)
os.system('ssh {}@192.168.1.58 bash < ./mariadb.sh'.format(user))
time.sleep(5)

print("Transfert du fichier de conf apache2")
ssh(log, 'sudo rm /etc/php/7.3/apache2/php.ini')
time.sleep(3)

os.system('scp php.ini {}@192.168.1.58:/home/{}'.format(user, user))
time.sleep(3)

ssh(log, 'sudo mv /home/{}/php.ini /etc/php/7.3/apache2/'.format(user))
ssh(log, RebootApache)

ssh(log, 'sudo apt-get install php-apcu')
ssh(log, 'sudo apt-get install php-ldap')
ssh(log, 'sudo apt-get install php-mysql')

print("...........90%")
print("Configuration silencieuse de GLPI..")
os.system('ssh {}@192.168.1.58 bash < ./glpi_install.sh'.format(user))
time.sleep(5)

 #Suppression du fichier install.php par sécuritée
ssh(log, 'sudo rm /var/www/html/glpi/install/install.php')
print("...........95%")
time.sleep(5)
ssh(log , 'sudo rm /var/tmp/glpi-9.4.5.tgz'.format(user))
ssh(log, RebootApache)
print("...........100%")
print("Deconnexion du serveur..")