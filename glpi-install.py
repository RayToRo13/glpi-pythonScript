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

#Connection au serveur sous le format glpi-install.py IP USERNAME PASSWORD /chemin du fichier yaml/fichier.yml
#L'appel de la def à besoin du/des packages que l'on souhaite installer, ils sont dans le fichier package.yml
def ssh(log, myCommand):
    
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=ip, username=user_name, password=passwd)
    s.exec_command('{}'.format(myCommand))
    time.sleep(25)
    s.close()            
        

def yaml():
#lis le fichier package.yml
  import yaml
  fichier = sys.argv[4]
  with open(fichier) as p:
    paquets = yaml.safe_load(p)
    return paquets
    variable = yaml()
    var = ' '.join(variable["packages"]["exec"])
#lecture des valeurs de la liste "exec" sous forme de string sans caractères spéciaux.
    print(var)
                    
##################################VARIABLES################################
Vars = yaml()

#Déclaration de mes variables pour simplification
#Lecture des listes dans le dictionnaire yaml
php1 = ' '.join(Vars["packages"]["php1"])
PaquetsPhp1 = 'sudo apt-get install {} -y'.format(php1)

php2 = ' '.join(Vars["packages"]["php2"])
PaquetsPhp2 = 'sudo apt-get install {} -y'.format(php2)

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
ssh(log, 'sudo wget -P /home/manu https://github.com/glpi-project/glpi/releases/download/9.4.5/glpi-9.4.5.tgz')   
time.sleep(15)

print("Téléchargement de GLPI..")
print("Mise à jour du système")
time.sleep(20)

ssh(log, update)
print("...........5%")
print("Installation des modules LAMP")
ssh(log, RebootApache)
time.sleep(20)

print("...........10%")
print("installation des modules php..")
#Re-installation des modules pour valider les intallations
ssh(log, PaquetMariaDB)
ssh(log, PaquetsPhp2)
ssh(log, RebootApache)
print("...........25%")
print("Redémarrage du service MariaDB")
ssh(log, PaquetsPhp1)
time.sleep(45)

print("...........35%")
ssh(log, ChGrpGLPI)
print("...........50%")
ssh(log, RebootApache)
print ("Redémarrage de apache2")
time.sleep(35)

ssh(log, 'sudo tar xvzf /home/manu/glpi-9.4.5.tgz -C /var/www/html')
time.sleep(20)

print("...........60%")
ssh(log, RebootApache)
print("Configuration finale de GLPI")
print("...........70%")
ssh(log, PaquetsPhp1)
ssh(log, DroitsGLPI)
ssh(log, ChGrpGLPI)
print("...........85%")
ssh(log, RebootApache)
os.system('ssh manu@192.168.1.58 bash < ./mariadb.sh')
time.sleep(3)

print("Transfert du fichier de conf apache2")
ssh(log, 'sudo rm /etc/php/7.3/apache2/php.ini')
time.sleep(3)

os.system('scp php.ini manu@192.168.1.58:/home/manu')
time.sleep(3)

ssh(log, 'sudo mv /home/manu/php.ini /etc/php/7.3/apache2/')
ssh(log, PaquetsPhp2)
ssh(log, RebootApache)
ssh(log, 'sudo apt-get install php-ldap')
time.sleep(15)

ssh(log, 'sudo apt-get install php-mysql')
print("...........90%")
print("Configuration silencieuse de GLPI..")
os.system('ssh manu@192.168.1.58 bash < ./glpi_install.sh')
time.sleep(30)

 #Suppression du fichier install.php par sécuritée
ssh(log, 'sudo rm /var/www/html/glpi/install/install.php')
print("...........95%")
time.sleep(5)

ssh(log, RebootApache)
print("...........100%")
print("Deconnexion du serveur..")
time.sleep(3)

print("Connection terminée")

