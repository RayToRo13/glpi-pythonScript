#!/usr/bin/env python3
import os
import sys
import paramiko
import time
import yaml

#id de connection
user_name=sys.argv[2]
passwd=sys.argv[3]
ip=sys.argv[1]
s=paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.connect(hostname=ip, username=user_name, password=passwd )
cmd='sudo apt-get install ["item"] -y'

with open(r'/home/test/Documents/Python codes/package.yml') as file:
    packageInstall= yaml.load(file, Loader=yaml.FullLoader)
    
    for package in packageInstall.package():
        s.exec_command(cmd)
time.sleep(5)
print("Installation de apache2..")
time.sleep(5)
print("Lancement du daemon Apache")
time.sleep(5)
print("apache 2 installé")
s.close()
time.sleep(2)
print("Deconnexion du serveur..")
time.sleep(5)
print("Connection terminée")