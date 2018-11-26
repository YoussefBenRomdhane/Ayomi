# Ayomi project
Ce projet a été réalisé avec Django 1.8, Python 2.7 et Bootstrap 3.

## Features (Packages installés)
* Django     1.8
* pip        18.1
* Bootstrap 3.3.7
* virtualenv (taper `pip install virtualenv` pour l'installer)

## Configuration du Virtualenv
 * Créer: virtualenv <NOM_DE_VOTRE_ENV_V> 
 * Activer: Sous Linux: `source bin/activate` 
            Sous Windows: `Scripts\Activate`

## Database 
J'ai utilisé une base de données locale sqlite.

## URLs
* ``http://127.0.0.1:8000/Ayomi/index`` : pour accéder à la page de connexion
* ``http://127.0.0.1:8000/admin`` : pour accéder à la partie admin

## Templates
* ``base.html``
* ``header.html``
* ``footer.html``
* ``index.html``
* ``profil.html``

## Comment installer les dépendances et exécuter ?

1- Ouvrir le projet avec l'IDE PyCharm.

2- Cliquer `File | Settings`.

3- Dans le dialogue `Project Interpreter`, séléctionner le fichier `python.exe` sous le dossier `Scripts` sous l'emplacement de votre virtual environnement.

4- Cliquer sur `OK`.

5- Lancer la commande `python manage.py runserver` pour lancer le projet.

## NB
Pour se connecter, taper `youssef` dans le champ username et `azerty0000` dans le champ password.

