import sys

arguments = sys.argv[1:]

if len(arguments) != 2:
    print("erreur.")
    sys.exit()

dividend = int(arguments[0])
divisor = int(arguments[1])

if divisor == 0:
    print("erreur.")
    sys.exit()
if dividend < divisor:
    print("erreur.")
    sys.exit()

rest = (dividend % divisor)
result = (dividend / divisor)

print(f"résultat: {int(result)}")
print(f"reste: {rest}")