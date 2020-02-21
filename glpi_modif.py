#!/usr/bin/env python3
import time
#Connection au serveur sous le format glpi-test.py IP USERNAME PASSWORD
#L'appel de la def à besoin du package que l'on souhaite installer.
def conn_ssh(package):
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
    cmd1 = 'sudo apt-get install {} -y'.format(package)
    s.exec_command(cmd1)
    time.sleep(5)
    print("Installation ..")
    time.sleep(3)
    print("Lancement du daemon ")
    time.sleep(3)
    print("package suivant")
    s.close()
    
def install_glpi(glpi):
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
    cmd1 = 'sudo tar xvzf /home/{} -C /var/www/'.format(glpi)
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
    
    
wget_glpi('-P /home/ https://github.com/glpi-project/glpi/releases/download/9.4.5/glpi-9.4.5.tgz')   
print("Téléchargement de GLPI..")
conn_ssh('git mariadb-server apache2 bind9 php7.3 php7.3-zip php7.3-gd')
conn_ssh('php7.3-pspell php7.3-recode php7.3-tidy php7.3-xmlrpc php7.3-xsl')
conn_ssh('php7.3-mbstring php-gettext')
conn_ssh('php7.3-ldap php-cas php-apcu libapache2-mod-php7.3 php7.3-mysql')
conn_ssh('php7.3-intl php-pear php-imagick php7.3-imap php-memcache')
time.sleep(45)
install_glpi('glpi-9.4.5.tgz')
print("Création base de données GLPI..")

print("Deconnexion du serveur..")
time.sleep(3)
print("Connection terminée")
