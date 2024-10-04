
import sys

arguments = sys.argv[1:]

argument_count = 0
for arg in arguments:
    argument_count += 1

if argument_count != 1:
    print("Erreur, veuillez rentrer un string svp")
    sys.exit()

string = arguments[0]

if string.isdigit():
    print("Erreur, votre argument ne doit pas contenir uniqement des chiffres")
    sys.exit()

total_letters = 0
for char in string:
    total_letters += 1
print(total_letters)
