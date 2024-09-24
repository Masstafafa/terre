"""
Créez un programme qui affiche son nom de fichier.


Exemples d’utilisation :
$> node exo.js
exo.js

$> node crevette.js
crevette.js

"""
import sys

file_name = sys.argv[0]
path_file = file_name.split("/") 
print(path_file[-1])
