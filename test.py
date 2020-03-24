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
        print(exit_status)
        if exit_status == 0:
            print("paquet installé")
        else:
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
        
Vars = yaml()
       
for key, data in (Vars['packages'].items()):
        pack= ' '.join(data)
        myCommand = "sudo apt-get install "+ pack+ " -y"
        print(myCommand)
        ssh(log, myCommand)      
    
