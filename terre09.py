import sys

arguments = sys.argv[1:]

if len(arguments) != 1:
    print("Erreur : Merci d'indiquer un seul argument")
    sys.exit()

if not arguments[0].isdigit():
    print("Erreur : Merci d'indiquer un chiffre")
    sys.exit()

number = int(arguments[0])

def square_root(number):
    if number < 2:
        return number
    counter = 1
    while counter * counter <= number:
        counter += 1
    return counter - 1
 

print(square_root(number))