#!/usr/bin/env python3
import os
import sys
import paramiko
import time
import yaml

ip = sys.argv[1]
user_name = sys.argv[2]
passwd = sys.argv[3]

#Connection au serveur sous le format glpi-install.py IP USERNAME PASSWORD
#L'appel de la def à besoin du/des packages que l'on souhaite installer, ils sont dans le fichier package.yaml
def conn_ssh(ip, user_name, passwd, myCommand):
    
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=ip, username=user_name, password=passwd)
    s.exec_command(myCommand)
    time.sleep(21)
    s.close()            
        
def yaml():
#lis le fichier package.yml
  import yaml
  with open(r'/home/test/Documents/Python_codes/package.yml') as p:
    paquets = yaml.safe_load(p)
    return paquets
    variable = yaml()
    var = ' '.join(variable["packages"]["exec"])
#lecture des valeurs de la liste "exec" sous forme de string sans caractères spéciaux.
    print(var)
    
def install_glpi(glpi):
    
    ip = sys.argv[1]
    user_name = sys.argv[2]
    passwd = sys.argv[3]
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=ip, username=user_name, password=passwd)
    cmd1 = '{}'.format(glpi)
    s.exec_command(cmd1)
    time.sleep(5)
    print("Installation de GLPI")
    time.sleep(6)
            
def install(install):
    
    ip = sys.argv[1]
    user_name = sys.argv[2]
    passwd = sys.argv[3]
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=ip, username=user_name, password=passwd)
    cmd1 = '{}'.format(install)
    s.exec_command(cmd1)
    time.sleep(11)
              

def wget_glpi(glpi):
    
    ip = sys.argv[1]
    user_name = sys.argv[2]
    passwd = sys.argv[3]
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=ip, username=user_name, password=passwd)
    cmd2 = 'sudo wget {}'.format(glpi)
    s.exec_command(cmd2)
    
   
def efface(efface):
   
    ip = sys.argv[1]
    user_name = sys.argv[2]
    passwd = sys.argv[3]
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=ip, username=user_name, password=passwd)
    cmd1 = '{}'.format(efface)
    s.exec_command(cmd1)
    s.close()

#Lien vers la dernière version de glpi|Modifier si nécessaire.   
wget_glpi('-P /home/manu https://github.com/glpi-project/glpi/releases/download/9.4.5/glpi-9.4.5.tgz')   
time.sleep(10)
print("Téléchargement de GLPI..")
#Conversion en variables pour les paramètres des def
Vars = yaml()
php1 = ' '.join(Vars["packages"]["php1"])
php2 = ' '.join(Vars["packages"]["php2"])
apache2 = ' '.join(Vars["packages"]["exec"])
mariadb = ' '.join(Vars["packages"]["exec2"])
com1 = ' '.join(Vars["packages"]["commande"])
com2 = ' '.join(Vars["packages"]["commande2"])
com3 = ' '.join(Vars["packages"]["commande3"])
update = ' '.join(Vars["packages"]["commande4"])
maCommand = 'sudo apt-get install {} -y'.format(apache2)
maCommand7 = 'sudo apt-get install {} -y'.format(mariadb)
maCommand2 = 'sudo apt-get install {} -y'.format(php1)
maCommand8 = 'sudo apt-get install {} -y'.format(php2)
CpFichier = 'sudo mv /home/manu/php.ini /etc/php/7.3/apache2/'
ldap = 'sudo apt-get install php-ldap'
mysql = 'sudo apt-get install php-mysql'

#on update & upgrade le serveur distant
#Mise à jour paquets
print("Mise à jour du système")
maCommand6 = '{}'.format(update)
#Restart apache2

maCommand3 = '{}'.format(com1)
#Droits pour v/var/www/html
maCommand4 = '{}'.format(com2)
#Changement Groupe www-data pour le dossier /var/www/html
maCommand5 = '{}'.format(com3)

conn_ssh(ip, user_name, passwd, maCommand6)
print("...........5%")
print("Installation des modules LAMP")
conn_ssh(ip, user_name, passwd, maCommand)

time.sleep(20)
print("...........10%")
print("installation des modules php..")
#Re-installation des modules pour valider les intallations
conn_ssh(ip, user_name, passwd, maCommand7)
conn_ssh(ip, user_name, passwd, maCommand8)
conn_ssh(ip, user_name, passwd, maCommand3)
print("...........25%")
print("Redémarrage du service MariaDB")
conn_ssh(ip, user_name, passwd, maCommand2)
time.sleep(45)


print("...........35%")

conn_ssh(ip, user_name, passwd, maCommand5)
print("...........50%")
conn_ssh(ip, user_name, passwd, maCommand3)
print ("Redémarrage de apache2")
time.sleep(35)

install_glpi('sudo tar xvzf /home/manu/glpi-9.4.5.tgz -C /var/www/html')
time.sleep(15)
print("...........60%")
conn_ssh(ip, user_name, passwd, maCommand3)
print("Configuration finale de GLPI")
print("...........70%")
conn_ssh(ip, user_name, passwd, maCommand2)
conn_ssh(ip, user_name, passwd, maCommand4)
conn_ssh(ip, user_name, passwd, maCommand5)
print("...........85%")
conn_ssh(ip, user_name, passwd, maCommand3)

os.system('ssh manu@192.168.1.58 bash < ./mariadb.sh')
time.sleep(3)
print("Transfert du fichier de conf apache2")
efface('sudo rm /etc/php/7.3/apache2/php.ini')
time.sleep(3)
os.system('scp php.ini manu@192.168.1.58:/home/manu')
time.sleep(3)
conn_ssh(ip, user_name, passwd, CpFichier)
conn_ssh(ip, user_name, passwd, maCommand8)
conn_ssh(ip, user_name, passwd, maCommand3)
install(ldap)
time.sleep(5)
install(mysql)
print("...........90%")
print("Configuration silencieuse de GLPI..")
os.system('ssh manu@192.168.1.58 bash < ./glpi_install.sh')
time.sleep(30)
RmInstallGlpi = 'sudo rm /var/www/html/glpi/install/install.php'
conn_ssh(ip, user_name, passwd, RmInstallGlpi)
print("...........95%")
time.sleep(5)
conn_ssh(ip, user_name, passwd, maCommand3)
print("...........100%")
#### mariaDB
print("Deconnexion du serveur..")
time.sleep(3)
print("Connection terminée")
