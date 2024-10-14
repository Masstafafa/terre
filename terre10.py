import sys

arguments = sys.argv[1:]

if len(arguments) != 1:
    print("Erreur : Merci d'indiquer un seul argument")
    sys.exit()

if not arguments[0].isdigit():
    print("Erreur : Merci d'indiquer un chiffre")
    sys.exit()

number = int(arguments[0])
counter_divisor = 0

for i in range(1, number+1):
    if number % i == 0:
        counter_divisor += counter_divisor
if counter_divisor == 2:
    print(f"Oui, {number} est un nombre premier.")
else:
    print(f"Non, {number} n'est pas un nombre premier.")


