"""Créez un programme qui affiche les arguments qu’il reçoit ligne par ligne, peu importe le nombre d’arguments.


Eemples d’utilisation :
$> ruby exo.rb je suis solide !
je
suis
solide
!"""

import sys

for words in sys.argv[1:]:
    print(words)