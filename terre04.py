import sys

arguments = sys.argv[1:]
print(arguments)

if not arguments:
    print("Tu ne me la mettras pas à l’envers.")
    sys.exit()

if not arguments[0].isdigit():
    print("Tu ne me la mettras pas à l’envers.")
    sys.exit()

number = int(arguments[0])

if number % 2 == 0:
    print("pair\n")
else:
    print("impair\n")