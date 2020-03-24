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

def yaml_paquets():
    #lis le fichier package.yml
  import yaml
  fichier = sys.argv[4]
  try :
        with open(fichier) as p:
            paquets = yaml.safe_load(p)
            return paquets
            variable = yaml_paquets()
            var = ' '.join(variable["packages"]["exec"])
#lecture des valeurs de la liste "exec" sous forme de string sans caractères spéciaux.
            return var
  except :
      print ("Fichier yaml inexistant, vérifier son nom")
      exit()
      
        
def ssh(log, myCommand):
    
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try :
        
        s.connect(hostname=ip, username=user_name, password=passwd)
        
        stdin, stdout, stderr = s.exec_command('{}'.format(myCommand))
        exit_status = stdout.channel.recv_exit_status()
        return exit_status
        if exit_status == 1:
            print("Erreur", exit_status)  
            print(stdout) 
    
        s.close()
    except :
        e = sys.exc_info()
        print(e)
        print ("Erreur de connexion...")
        time.sleep(1)
        print ("Veuillez vérifier vos paramètres...")
        time.sleep(1)
        exit()            
        
##################################VARIABLES################################            
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

print("Mise à jour du système client..\n")
   
ssh(log, update)

print ("Installation des paquets:\n")
      
for key, data in (Vars['packages'].items()):
        pack= ' '.join(data)
        myCommand = "sudo apt-get install "+ pack+ " -y"
        print(pack)
        ssh(log, myCommand)

ssh(log, 'sudo wget -P /var/tmp https://github.com/glpi-project/glpi/releases/download/9.4.5/glpi-9.4.5.tgz')
print("Téléchargement de GLPI..")

ssh(log, 'sudo tar xvzf /var/tmp/glpi-9.4.5.tgz -C /var/www/html')
ssh(log, RebootApache)
ssh(log, ChGrpGLPI)
ssh(log, DroitsGLPI)
os.system('ssh {}@192.168.1.58 bash < ./mariadb.sh'.format(user))
print("Transfert du fichier de conf apache2")
ssh(log, 'sudo rm /etc/php/7.3/apache2/php.ini')
os.system('scp php.ini {}@192.168.1.58:/home/{}'.format(user, user))
ssh(log, 'sudo mv /home/{}/php.ini /etc/php/7.3/apache2/'.format(user))
ssh(log, RebootApache)
print("Configuration silencieuse de GLPI..")
os.system('ssh {}@192.168.1.58 bash < ./glpi_install.sh'.format(user))

#Suppression du fichier install.php
ssh(log, 'sudo rm /var/www/html/glpi/install/install.php')
ssh(log , 'sudo rm /var/tmp/glpi-9.4.5.tgz'.format(user))
ssh(log, RebootApache)
print("Deconnexion du serveur..")