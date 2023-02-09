<a name="readme-top"></a>

# CI/CD PROJET


<p align="center">
  <img src="https://user-images.githubusercontent.com/93181410/166483696-8a4daae2-d6e3-4a61-b425-f5118cc6e085.png" width="300"/>
  <img src="https://user-images.githubusercontent.com/93181410/210587101-8d27cb1b-14ed-4bad-8c16-a579c4ad7289.png" width="180"/>
</p>

4A IE SQR TP1  
OUTSSAKKI Anisse et EL ALOUANI Naofel

## Présentation du projet

**Objectif :** Créer une API Flask pour de la gestion CRUD d’un système de transaction

**Langage :** [![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

**Sujet choisi:** Sujet guidé - Un chemin tout tracé

Nous avons choisi ce sujet car nous avons préféré être encadré. En effet, ceci est nouveau pour nous et nous n'aurons pas pu progressé sans être un minimum guidé.


## Technologie utilisée
### Flask 
Flask est un micro framework web gratuit et open-source pour Python conçu pour aider les développeurs à construire des applications web sécurisées, évolutives et maintenables. Flask est basé sur Werkzeug et utilise Jinja2 comme moteur de template. Il nécessite donc d'avoir déjà Python3 installé.

### Installation :
Que ce soit sur Windows ou Linux, la commande permettant son installation est : 

```
pip install flask
```

On verifie ensuite les versions en cours:

```
python -m flask --version
```
Dans notre cas, voici les versions que nous avons :
```
Python 3.8.10
Flask 2.2.2
Werkzeug 2.2.2
```

### Utilisation :
Après avoir créer notre API dans un fichier Python nous pouvons effectuer des tests unitaires en demarrant le serveur flask ainsi :

**Sur Linux**
```
export FLASK_APP=TP.py
export FLASK_ENV=development
flask run
```
**Sur Windows**
```
set FLASK_APP=TP.py
set FLASK_ENV=development
flask run
```
Ensuite, depuis notre navigateur web, un logiciel tel qu'insomnia ou en ligne de commande nous pouvons tester notre API avec les commandes suivantes.
Pour notre premier endpoint utilisant une methode POST:
```
curl -X POST http://localhost:5000/add
```

Ou encore celle-ci, pour notre quatrième route utilisant une méthode GET et intégrant un ID dans l'URL:
```
curl -X GET http://localhost:5000/solde/1
```

Mais aussi, celle notre dernière route important les données d'un fichier csv:
```
curl -X POST -F 'transactions=@transactions.csv' http://localhost:5000/csv
```

### Algorithme de hachage
Nous avons choisi la fonction de hachage **SHA-256** dans nos transactions qui est notamment utilisé par Bitcoin pour garantir l'intégrité des informations stockées dans un bloc. Desormais, le modèle des transactions sera composé ainsi: (P1, P2, t, s, h), où **s** est égal à la somme d’argent transférée de la personne **P1** à la personne **P2** à l’instant **t** et **h** correspond au hash de P1, de P2, et s.
SHA-256 est l'un des plus utilisés en raison de son équilibre entre la sécurité et le coût de calcul de la génération, car il s'agit d'un algorithme très efficace pour la résistance élevée aux collisions dont il dispose. Il garantit que cet algorithme sera sûr pendant très longtemps, au moins 20 ans.

Prenons l'exemple suivant: P1(id=1) envoie 1 500 euros à P2(id=2), en suivant la structure de notre fichier csv voici ci-dessous le resultat de la fonction de hachage de SHA-256
<p align="center">
  <img src="https://user-images.githubusercontent.com/93181410/216112844-c86df570-61a5-4ea3-bd50-6d74ae75c005.png" width="400"/>
</p>



## Contact

**Naofel** : 

[![GitHub][github-shield1]][github-url]     
[![LinkedIn Naofel][linkedin-shield]][linkedin-url]    
naofel_el-alouani@etu.u-bourgogne.fr


**Anisse** : 

[![GitHub][github-shield2]][github-url1]   
[![LinkedIn Anisse][linkedin-shield]][linkedin-url2]  
anisse_outssakki@etu.u-bourgogne.fr



## Statuts action

[![Pull Request Workflow](https://github.com/Naofel-eal/4A_SQR_CI-CD/actions/workflows/blank.yml/badge.svg)](https://github.com/Naofel-eal/4A_SQR_CI-CD/actions/workflows/blank.yml)

[Lien](https://github.com/Naofel-eal/4A_SQR_CI-CD/blob/main/.github/workflows/README.md) vers les badges des résultats des builds des dernières CI exécutées

[![](https://img.shields.io/badge/PROJET_TERMINÉ_🚀-059142?style=for-the-badge&logoColor=white)](https://dev.to/envoy_/150-badges-for-github-pnk) 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[img-valide]: https://cdn.pixabay.com/photo/2017/05/03/23/39/ok-2282499_960_720.png
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/naofel-el-alouani-83a947197/
[linkedin-url2]: https://www.linkedin.com/in/anisse-outssakki-101926199/
[github-shield1]: https://img.shields.io/github/followers/AnisseO?style=social
[github-shield2]: https://img.shields.io/github/followers/Naofel-eal?style=social
[github-url]: https://github.com/Naofel-eal
[github-url1]: https://github.com/AnisseO
[mail-shield]: https://www.icone-png.com/png/10/9870.png
