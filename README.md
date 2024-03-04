# Dépôt Git IS104 (Projet n°3)

## Organisation du dépôt

Le code du projet se trouve dans le répertoire **src**. Pour chaque partie, il y a un code correspondant nommé au numéro de sa partie.
Par exemple, le code de la partie 1 se trouve dans le fichier `part1.py`.
On y trouve aussi les différents fichiers de tests qui correspondent aux différentes parties.
Par exemple, les tests pour la partie 1 sont dans le fichier `test1.py`. 

Dans le répertoire **sections**, on peut trouver les différents fichiers latex correspondant aux différentes parties incluses dans le fichier `rapport.tex`.

## Makefile
Le **Makefile** dispose de plusieurs cibles, et permet en exécutant la commande `make test` de lancer des tests sur toutes les parties. 
La commande `make` permet de générer le rapport, et pour obtenir des détails sur la compilation du rapport, il faut lancer la commande `make verbose`.

## Partie 1 - Transformations de Householder
En exécutant `src/part1.py`, on effectue une comparaison du temps d'exécution de nos fonctions par rapport à des produits classiques de matrices classiques.

Le fichier `src/test1.py` vérifie que ces fonctions donnent des résultats proches de ceux attendus, avec un écart `eps` réglable.

## Partie 2 - Mise sous forme bidiagonale
Le fichier `src/part2.py` dispose seulement de fonctions, et agit comme un module par rapport aux parties suivantes.

Pour les tests, sur le fichier `src/test2.py`, on teste notre fonction de bidiagonalisation sur des matrices variées, en vérifiant que le résultat est bien une matrice bidiagonale, et que le produit des matrices renvoyées est proche à la matrice de départ, avec un écart `eps` que l'on peut modifier.

## Partie 3 - Transformations QR et SVD
L'exécution du fichier `src/part3.py` entraîne la génération d'une figure montrant la vitesse de convergence de la méthode de diagonalisation de matrice à partir d'une matrice bidiagonale.

En exécutant `src/test3.py`, on effectue des vérifications sur cette méthode de diagonalisation, ainsi que notre décomposition QR et notre fonction de SVD. Pour chacun des cas, on vérifie que les matrices renvoyées ont bien les caractéristiques attendues (matrice orthogonale, triangulaire supérieure, diagonale, ...).

## Partie 4 - Application de la SVD à la compression d'image
Cette partie utilise le fichier `res/part-4.png`, que l'on considère comme l'image _originale_. Exécuter ce fichier génère d'abord deux exemples de compression d'image utilisant la méthode SVD, en comparaison avec l'image originale.
Ensuite, une figure montre les distances à l'image originale, avec une échelle logarithmique.
Enfin, la dernière figure montre la taille du fichier en nombre de valeurs, par rapport au rang de la compression.

En ce qui concerne les tests, le fichier `src/test-4.py` vérifie que les images après compression sont bien proches des images compressées fournies.