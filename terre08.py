import sys

arguments = sys.argv[1:]

if len(arguments) != 2:
    print("Erreur : Merci de ne rentrer que deux arguments qui doivent être des chiffres")
    sys.exit()

for arg in arguments:
    try:
        number_check = int(arg)
    except ValueError:
        print("Erreur : pour nombre et puissance, veuillez entrer deux nombres.")
        sys.exit()

number = int(arguments[0])
power = int(arguments[1])

if power == 0:
    print("1")
    sys.exit()

result = 1
for i in range(power):
    result *= number
print(result)