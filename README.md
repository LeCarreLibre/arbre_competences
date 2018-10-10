# Arbre des competences

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/bb24e635ff1b489380ddf43c869e6f7c)](https://app.codacy.com/project/Le_Carre_Libre/arbre_competences/dashboard)
[![Code Health](https://landscape.io/github/nils-van-zuijlen/arbre_competences/master/landscape.svg?style=flat)](https://landscape.io/github/nils-van-zuijlen/arbre_competences/master)

------------

## Contribuer
Les contributions sont acceptées avec joie, cependant, les commits ne doivent contenir qu'une seule modification majeure et ne doivent JAMAIS être réalisés sur la branche ´master´. Toutes les pull-request doivent passer les tests et ne contenir qu'une seule fonctionnalité. Seul le propriétaire du repository peut valider celles qui pointent vers ´master´.

Pour pouvoir créer et utiliser un environnement il est recommandé d'utiliser pipenv.  
Si vous souhaitez seulement créer un environnement de production il vous faudra faire la commande `pipenv install`  
Pour préparer votre environnement de développement vous devrez faire la commande `pipenv install -d` pour installer les dépendances nécessaires au développement.  
Une fois les dépendances installées il vous suffira de passer la variable `DEBUG` à `True` dans le fichier `arbre_competences/settings.py`.
