#!/usr/bin/env python3
import os
import sys
import paramiko
import time
import yaml

ip = sys.argv[1]
user_name = sys.argv[2]
passwd = sys.argv[3]

#Connection au serveur sous le format glpi-test.py IP USERNAME PASSWORD
#L'appel de la def à besoin du package que l'on souhaite installer.
def conn_ssh(ip, user_name, passwd, myCommand):
    
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=ip, username=user_name, password=passwd)
    s.exec_command(myCommand)
    time.sleep(3)
    print("Installation .")
    time.sleep(3)
    print("Installation .. ")
    time.sleep(3)
    print("Installation ...")
    time.sleep(10)
    s.close()            
        
    
def yaml():
    #lis le fichier package.yml.
    import yaml
    with open(r'/home/test/Documents/Python_codes/package.yml') as p:
        paquets = yaml.safe_load(p)
        return paquets
        variable = yaml()
        var = ' '.join(variable["packages"]["commande"])
        #lecture des valeurs de la liste "rest" sous forme de string sans caractères spéciaux.
        print(var)
  
Vars = yaml()
RmInstallGlpi = 'sudo rm /var/www/html/glpi/install/install.php'

#on update & upgrade le serveur distant
com1 = ' '.join(Vars["packages"]["commande"])
maCommand3 = '{}'.format(com1)
conn_ssh(ip, user_name, passwd, RmInstallGlpi)
print("...........50%")
conn_ssh(ip, user_name, passwd, maCommand3)

print("Deconnexion du serveur..")
time.sleep(3)
print("Connection terminée")
