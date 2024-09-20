"""
Créez un programme qui affiche l’alphabet en lettres minuscules suivi d’un retour à la ligne.

Exemples d’utilisation :
$> python exo.py
abcdefghijklmnopqrstuvwxyz
$>

Attention : votre programme devra utiliser une boucle.

"""
#Valeur ascii a = 97 et z = 122. Faire en sorte de faire 
#une boucle puis ensuite d'imprimer chacun des caractères
a = 97
z = 122
for alphabet in range (97, 122 + 1):
    print(chr(alphabet), end="")
print()
