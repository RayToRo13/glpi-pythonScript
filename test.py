#!/usr/bin/env python3
import yaml
import time
import sys

def yaml():
    #lis le fichier package.yml
  import yaml
  with open(r'/home/test/Documents/script/package.yml') as p:
    paquets = yaml.safe_load(p)
    return paquets
    variable = yaml()
    var = ' '.join(variable["packages"]["exec"])
    return var

Vars = yaml()

for key, data in (Vars['packages'].items()):
        test= ' '.join(data)
        print("sudo apt-get install", test, "-y")
        time.sleep(5)
