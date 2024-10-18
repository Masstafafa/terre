import sys

arguments = sys.argv[1:]

if len(arguments) != 3:
    print("Erreur : Merci de rentrer trois arguments")
    sys.exit()

if not all(number.isdigit() for number in arguments):
    print("Erreur : Merci d'indiquer trois chiffres")
    sys.exit()

number_1 = int(arguments[0])
number_2 = int(arguments[1])
number_3 = int(arguments[2])

if number_1 == number_2 == number_3:
    print("Erreur")

if number_2 < number_1 < number_3:
    print(number_1)
elif number_1 < number_2 < number_3:
    print(number_2)
elif number_1 < number_3 < number_2:
    print(number_3)
