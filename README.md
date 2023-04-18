# Insta Paper

Ce dépôt contient le projet de session du cours GLO-2005 durant la session d'hiver 2023 à l'Université Laval. 

## Contenu du dépôt

Le dépôt se compose de 3 parties :

 - La base de données (MySQL), conteneurisée, avec des valeurs par défaut.
 - Le serveur (Python), servant une API avec Flask.
 - L'application Web (NextJS).
 
## Build & Utilisation
 
Pour respecter les dépendances entre les services, il est recommandé de lancer les services dans l'ordre suivant.

### Base de données

Le contexte se situe dans `/sources/database`.

Des scripts contenants des données par défaut sont présents dans le dossier  `init_scripts`, et sont chargés dans le conteneur docker automatiquement.

Pour lancer la base de données, exécuter la commande `docker-compose up --build database` .

### Serveur

Le contexte est se situe dans `/sources/backend`.

Il est conseillé d'utiliser un environnement virtuel comme `venv` pour éviter d'installer les dépendances globalement. L'environnement virtuel doit être lancé avant le script de build.

Un script est présent qui se chargera d'installer les dépendances, de build le serveur, et de le lancer. Pour cela exécuter le script `./build_and_run.sh`. Le serveur sera ensuite accessible sur le port `5000`.

### Application Web

Le contexte est se situe dans `/sources/frontend`.

L'application web a été construite en utilisant `NextJS 13`, `Node` doit donc être installé sur la machine pour le build. La version conseillée est `v16`.

Pour que l'application soit fonctionnelle, il est nécessaire de lui indiquer l'adresse du serveur backend dans le fichier `.env.local`. Un fichier d'exemple est présent dans le dépôt, à vous de le renommer.

La commande `npm run build` se chargera de build l'application, puis on pourra exécuter la commande `npm run start` pour la rendre accessible sur le port `3000`.

---

* [<img src="https://avatars.githubusercontent.com/u/74084836?v=4" alt="drawing" width="32" height="32"/> Lauriane Blouin](https://github.com/lolo77929)
* [<img src="https://avatars.githubusercontent.com/u/61425306?v=4" alt="drawing" width="32" height="32"/> Baptiste Renouf](https://github.com/Tsaef)
* [<img src="https://avatars.githubusercontent.com/u/60100363?v=4" alt="drawing" width="32" height="32"/> Luann Bertaud](https://github.com/luannbertaud)