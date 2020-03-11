#!/usr/bin/env python3
def yaml():
    #lis le fichier package.yml
  import yaml
  with open(r'/home/test/Documents/script/package.yml') as p:
    paquets = yaml.safe_load(p)
    return paquets
    variable = yaml()
    var = ' '.join(variable["packages"]["exec"])
#lecture des valeurs de la liste "exec" sous forme de string sans caractères spéciaux.
    print(var)

Vars = yaml()
com2 = ' '.join(Vars["packages"]["commande2"])
print(com2)