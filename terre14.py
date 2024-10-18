import sys

arguments = sys.argv[1:]

if not all(arg.isdigit() for arg in arguments):
    print("Erreur : Merci d'indiquer des chiffres uniquement")
    sys.exit()

all_number = list(map(int, arguments))

sorted = True
for i in range(len(all_number) - 1):
    if all_number[i] > all_number[i + 1]:
        not_sorted = False
        break
        
if sorted:       
    print("Triée!")
else:
    print("Pas triée!")   


        



