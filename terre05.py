import sys

arguments = sys.argv[1:]
#dividend = int(arguments[0])
#divisor = int(arguments[1])

if len(arguments) != 2:
    print("erreur.")
    sys.exit()

try:
    dividend = int(arguments[0])
    divisor = int(arguments[1])
except ValueError:
    print("erreur: les arguments doivent être des entiers.")
    sys.exit()

if divisor == 0:
    print("erreur.")
    sys.exit()
if dividend < divisor:
    print("erreur.")
    sys.exit()

#rest = int(dividend % divisor)
#result = int(dividend / divisor)


print(f"résultat: {result}")
print(f"reste: {rest}")