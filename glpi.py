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
    time.sleep(5)
    print("Installation ..")
    time.sleep(3)
    print("Lancement du daemon ")
    time.sleep(3)
    print("package suivant")
    s.close()
    

def hote_ip():
    #lis le fichier package.yml.
    import yaml
    with open(r'/home/test/Documents/Python codes/package.yml') as p:
        paquets = yaml.safe_load(p)
        return paquets
        variable = yaml()
        var = ' '.join(variable["packages"]["rest"])
        #lecture des valeurs de la liste "rest" sous forme de string sans caractères spéciaux.
        print(var)

def hote_user():
    #lis le fichier package.yml.
    import yaml
    with open(r'/home/test/Documents/Python codes/package.yml') as p:
        paquets = yaml.safe_load(p)
        return paquets
        variable = yaml()
        var = ' '.join(variable["packages"]["rest"])
        #lecture des valeurs de la liste "rest" sous forme de string sans caractères spéciaux.
        print(var)

def hote_pass():
    #lis le fichier package.yml.
    import yaml
    with open(r'/home/test/Documents/Python codes/package.yml') as p:
        paquets = yaml.safe_load(p)
        return paquets
        variable = yaml()
        var = ' '.join(variable["packages"]["rest"])
        #lecture des valeurs de la liste "rest" sous forme de string sans caractères spéciaux.
        print(var)


def yaml_paquets_php():
    #lis le fichier package.yml.
    import yaml
    with open(r'/home/test/Documents/Python codes/package.yml') as p:
        paquets = yaml.safe_load(p)
        return paquets
        variable = yaml()
        var = ' '.join(variable["packages"]["php"])
        #lecture des valeurs de la liste "rest" sous forme de string sans caractères spéciaux.
        print(var)




def yaml_paquets_LAMP():
    #lis le fichier package.yml.
    import yaml
    with open(r'/home/test/Documents/Python codes/package.yml') as p:
        paquets = yaml.safe_load(p)
        return paquets
        variable = yaml()
        var = ' '.join(variable["packages"]["rest"])
        #lecture des valeurs de la liste "rest" sous forme de string sans caractères spéciaux.
        print(var)
    
def install_glpi(glpi):
    user_name = sys.argv[2]
    passwd = sys.argv[3]
    ip = sys.argv[1]
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=ip, username=user_name, password=passwd)
    cmd1 = '{}'.format(glpi)
    s.exec_command(cmd1)
    time.sleep(5)
    print("Installation ..")
    time.sleep(3)
    print("Lancement du daemon ")
    time.sleep(3)
    print("package suivant")
    s.close()             
   
def wget_glpi(glpi):
    import os
    import sys
    import paramiko
    import time
    user_name = sys.argv[2]
    passwd = sys.argv[3]
    ip = sys.argv[1]
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=ip, username=user_name, password=passwd)
    cmd2 = 'wget {}'.format(glpi)
    s.exec_command(cmd2)
    
def mariadb(script):
    user_name = sys.argv[2]
    passwd = sys.argv[3]
    ip = sys.argv[1]
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=ip, username=user_name, password=passwd)
    cmd2 = './'.format(glpi)
    s.exec_command(cmd2)

    
wget_glpi('-P /home/ https://github.com/glpi-project/glpi/releases/download/9.4.5/glpi-9.4.5.tgz')   
print("Téléchargement de GLPI..")
Vars = yaml()
mesPackages = ' '.join(Vars["packages"])
maCommand = 'sudo apt-get install {} -y'.format(mesPackages)
conn_ssh(ip, user_name, passwd, maCommand)

time.sleep(45)
install_glpi('sudo tar xvzf /home/glpi-9.4.5.tgz -C /var/www/')
print("Création base de données GLPI..")


print("Deconnexion du serveur..")
time.sleep(3)
print("Connection terminée")
