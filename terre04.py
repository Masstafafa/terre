"""Créez un programme qui permet de déterminer si l’argument donné est un entier pair ou impair..


Exemples d’utilisation :
$> ruby exo.rb 2
pair

$> ruby exo.rb 5
impair


$> ruby exo.rb Bonjour
Tu ne me la mettras pas à l’envers.

$> ruby exo.rb
Tu ne me la mettras pas à l’envers.


Attention : gérez aussi les entiers négatifs.

Fonctions interdites: 
-En Ruby: even? et odd?"""

import sys

if len(sys.argv) < 2:
    print("Tu ne me la mettras pas à l’envers.")
    sys.exit(0)

user_choice = sys.argv[1]

if not user_choice.isdigit():
    print("Tu ne me la mettras pas à l’envers.")
elif int(user_choice) % 2 == 0:
    print("pair\n")
elif int(user_choice) % 2 != 0:
    print("impair\n")



