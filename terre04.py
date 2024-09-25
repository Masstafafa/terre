import sys

if len(sys.argv) < 2:
    print("Tu ne me la mettras pas à l’envers.")
    sys.exit(0)

user_choice = sys.argv[1]

if not user_choice.isdigit():
    print("Tu ne me la mettras pas à l’envers.")
elif int(user_choice) % 2 == 0:
    print("pair\n")
elif int(user_choice) % 2 != 0:
    print("impair\n")



