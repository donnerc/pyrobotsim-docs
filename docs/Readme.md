run
# Documentation du TM informatique 2022-2023 (Développement Web)

## Installation des dépendances

Dans ce projet, les dépendances sont gérées grâce à `poetry`. Il faut donc
commencer par installer le gestionnaire de packages Python `poetry` avec 

```{bash}
curl -sSL https://install.python-poetry.org | python3 -
```

On peut ensuite installer les dépendances avec 

```{bash}
poetry install
```



## Configuration de Sphinx

Il faut insérer vos informations (auteur, titre, ... ) dans le fichier
`source/tmconfig.py`. Ce fichier est ensuite automatiquement importé dans le module `conf.py` qui permet de configurer Sphinx.

## Génération des documents cibles

### Compilation en HTML

Pour compiler les fichiers Sphinx en HTML, il faut entrer la commande suivante depuis le dossier racine du projet contenant le fichier `Makefile` :

```bash
make livehtml
```

### Compilation en LaTeX (PDF)

Pour pouvoir générer le PDF, il faut au préalable installer LaTeX sur le système. Sur un système Linux, il suffit de faire les commandes

```bash
sudo apt update
sudo apt-get install texlive-latex-extra texlive-lang-french texlive-fonts-recommended latexmk
```

Sur les machines Windows, l'installation risque d'être plus compliquée, raison pour laquelle il est conseillé de compiler votre travail directement dans Cloud9 ou dans le Bash Ubuntu de Windows 10.

Ensuite, pour générer le PDF, il suffit de faire depuis la racine du dépôt où se trouve le fichier `Makefile` principal :

```bash
make tmpdf
```

et de se rendre dans le dossier `build/latex/` et ouvrir le fichier `tm-ecrit.pdf` généré par LaTeX.

## Visualisation des pages HTML générées

### Depuis une machine de développement locale

Il suffit ensuite, pour visualiser le résultat, de visiter http://localhost:8000/ dans le navigateur Web.

## Cloner le dépôt

Le plus simple, pour démarrer, est de forker ce dépôt dans votre propre compte
GitHub et cloner ce dernier sur votre machine locale ou dans un IDE en ligne tel
que Gitpod.

## Édition en ligne avec gitpod.io

L'IDE en ligne Gitpod permet de disposer de machines virtuelles complètes sur
lesquelles faire tourner la chaines d'outils Sphinx / LaTeX pour écrire la
documentation des projets de TM en informatique.

Voici les étapes à suivre:

1. Forker le dépôt https://github.com/informatiquecsud/sphinx-tm-template/ dans
   votre compte GitHub.

2. Ouvrir votre version du dépôt sur GitHub et, dans la barre d'adresse du
   navigateur Web, rajouter `https://gitpod.io#` tout à gauche de l'adresse de
   votre dépôt GitHub. Pour que cela fonctionne, vous devez avoir un compte sur
   la plateforme https://gitpod.io/.

3. Dans Gitpod, il faut commencer par installer Sphinx avec

   ```bash
   pip install -r requirements.txt
   ```

4. Vous pouvez ensuite générer le HTML avec

   ```bash
   make livehtml
   ```

5. Pour générer le PDF, il suffit d'exécuter la commande suivante dans un
   terminal.

   ```bash
   make tmpdf
   ```

## Installation de LaTeX

### Sur Gitpod

### Sur Linux Ubuntu