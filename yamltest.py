#!/usr/bin/env python3


def yaml():
    import yaml
    with open(r'/home/test/Documents/Python codes/package.yml') as packages:
        p = yaml.safe_load(packages)
        paquets = 'packages'.join(p)
        print(p)
        
yaml()