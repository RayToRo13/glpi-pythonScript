# Déploiement d'un glpi sur une machine distante

[![N|Solid](https://glpi-project.org/wp-content/uploads/2017/03/logo-glpi-bleu-1.png)](https://glpi-project.org/fr/) 

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger) version 1.0


# Conditions d'utilisation
  - Ubuntu 18.04
  - python3.8
  - pip3
  - Client sous debian
  - Sudo sans mot de passe en local et en distant
## Depuis pip install
  -paramiko2.7.1
  -yaml-1.3
  


### Sudo sans password : 
- $user = utilisateur avec lequel on va se connecter et éxécuter le script

éditer le fichier en root:
```
$ /etc/sudoers 
```
et y ajouter :
>$user ALL=(ALL) NOPASSWD: ALL

## Installations
#### python
Pré-requis
```sh
 $ sudo apt update
 $ sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
```
Téléchargement de python
```sh
$ cd /tmp
$ wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz
```
Extraction du .tgz et initiilisation de l'installation
```sh
$ tar -xf Python-3.8.0.tgz
$ cd Python-3.8.0
$ ./configure --enable-optimizations
```
Ensuite on lance ces commandes ( on remplace 1 par le nombre de Cores de son cpu)
```sh
$ make -j 1
$ sudo make altinstall
 ```
 Une fois terminé on vérifie sa version de python installée
```sh 
$ python3.8 --version
``` 

> Python 3.8.0


### dépendances
#### pip
```
$ sudo apt install python3-pip
```

#### yaml
```
$ pip3 install yaml-1.3
```
#### paramiko
```
$ pip3 install paramiko
```
* [doc paramiko](http://www.paramiko.org/installing.html)
# lancement du script

  - A executer avec l'user qui les droit sudo sans password en local
```sh
$ python3 glpi.py $ip $user_ssh $pass_user_ssh $package_yaml_a_utiliser
```
![](https://i.ibb.co/n8PGY4J/1.png)
 - Resultat finale après execution
![](https://i.ibb.co/WnJ3JRw/script-output.png)
 

### fonctionnement
Le script permet de déployer un glpi sur une machine distante. Il automatise :
 - le télechargement et l'installation d'apache2, mariadb, php7.3
 - téléchargement de glpi et installation
 - création base de donnée
 - installation silencieuse de glpi
 

## Erreurs de lancement
- Un contrôle de la bonne connection au serveur distant est prévu par le script.
Un problème d'ip username password en est en générale la cause

- une contrôle de la présence du fichier yaml
Le fichier yaml dans être présent dans le dossier du script (pas de chemin relationnel ou absolu)


### Contributions
Pour les contributions veuillez :
- fork le repository 
- git clone https://github.com/RayToRo13/glpi-pythonScript.git
- Créer une nouvelle branche pour les modifications (git checkout -b ma_nouvelle_branche)
- Commit vos modifications   (git commit -am 'Ajout de modifications')
- Push dans votre fork (git push origin Ajout de modifications)
- Créer une nouvelle pull request du fork afin que je puisse décider d'inclure ou non vos modifications

# Script réalisé dans le cadre d'un projet de parcours de formation sur
 [![N|Solid](https://blog.openclassrooms.com/wp-content/uploads/2018/05/OC.png)](https://openclassrooms.com/)
 


### License GNU General Public License v3.0
Vous pouvez disposer du script librement.



