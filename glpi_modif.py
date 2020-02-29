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
        var = ' '.join(variable["packages"]["exec"])
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
    print("Installation .")
    time.sleep(3)
    print("Installation .. ")
    time.sleep(3)
    print("Installation ...")
    #s.close()             
   
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
    cmd2 = 'sudo wget {}'.format(glpi)
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
    s.close()

    
wget_glpi('-P /home/manu https://github.com/glpi-project/glpi/releases/download/9.4.5/glpi-9.4.5.tgz')   
time.sleep(10)
print("Téléchargement de GLPI..")
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
#on update & upgrade le serveur distant
maCommand6 = '{}'.format(update)
maCommand3 = '{}'.format(com1)
maCommand4 = '{}'.format(com2)
maCommand5 = '{}'.format(com3)


conn_ssh(ip, user_name, passwd, maCommand6)
print("...........5%")
conn_ssh(ip, user_name, passwd, maCommand)

time.sleep(20)
print("...........10%")
print("installation modules php..")
conn_ssh(ip, user_name, passwd, maCommand7)
conn_ssh(ip, user_name, passwd, maCommand8)
conn_ssh(ip, user_name, passwd, maCommand3)
print("...........25%")
print("Installation MariaDB")
conn_ssh(ip, user_name, passwd, maCommand2)
time.sleep(45)


print("...........35%")
conn_ssh(ip, user_name, passwd, maCommand5)
print("...........50%")
conn_ssh(ip, user_name, passwd, maCommand3)

time.sleep(45)

install_glpi('sudo tar xvzf /home/manu/glpi-9.4.5.tgz -C /var/www/html')
print("...........60%")
conn_ssh(ip, user_name, passwd, maCommand3)
print("...........70%")
conn_ssh(ip, user_name, passwd, maCommand2)
conn_ssh(ip, user_name, passwd, maCommand4)
conn_ssh(ip, user_name, passwd, maCommand5)
print("...........85%")
conn_ssh(ip, user_name, passwd, maCommand3)
print("...........100%")
os.system('ssh manu@192.168.1.58 bash < ./mariadb.sh')

print("Création base de données GLPI..")

#### mariaDB
print("Deconnexion du serveur..")
time.sleep(3)
print("Connection terminée")
