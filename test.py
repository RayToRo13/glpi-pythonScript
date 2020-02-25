#!/usr/bin/env python3
import os
import sys
import paramiko
import time

#id de connection
user_name = sys.argv[2]
passwd = sys.argv[3]
ip = sys.argv[1]
s = paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.connect(hostname=ip, username=user_name, password=passwd)

cmd1 = 'sudo apt-get install apache2 -y'
#cmd2='sudo sh -c `apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y mariadb-server`'
s.exec_command(cmd1)
time.sleep(5)
print("Installation de mariadb & apache2..")
time.sleep(5)
print("Lancement du daemon Mysql & Apache")
time.sleep(5)
print("MariaDB & apache 2 installé")
s.close()
time.sleep(2)
print("Deconnexion du serveur..")
time.sleep(5)
print("Connection terminée")