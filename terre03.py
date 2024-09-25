"""Créez un programme qui affiche l’alphabet à partir de la lettre donnée en argument en lettres minuscules suivi d’un retour à la ligne.


Exemples d’utilisation :
$> python exo.py n
nopqrstuvwxyz
$>


Attention : votre programme devra utiliser une boucle."""

import sys

choice_letter = sys.argv[1]

for letter in range(ord(choice_letter), ord('z') + 1):
    print(chr(letter), end='')

print()
        
