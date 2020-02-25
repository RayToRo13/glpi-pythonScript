#!/usr/bin/env python3


def yaml():
    import yaml
    with open(r'/home/test/Documents/Python codes/package.yml') as p:
        paquets = yaml.safe_load(p)
        return paquets
    
variable = yaml()
var = ' '.join(variable["packages"]["rest"])
print(var)
