import sys
import re

arguments = sys.argv[1:]

if len(arguments) != 1:
    print("Erreur : Un seul argument doit être rentré")
    sys.exit()

full_hour = arguments[0].upper()

time_regex = "^(0[1-9]|1[0-2]):[0-5][0-9](AM|PM)$"

if not re.match(time_regex, full_hour):
    print("Erreur : l'heure ne peut être comprise qu'entre O et 12,"
          " les minutes ne peuvent être comprise qu'entre O et 59"
          " Merci d'indiquer l'horaire avec le format xx:xxAM/PM")
    sys.exit()

hours = int(full_hour[0:2])
minutes = int(full_hour[3:5])
meridiem = full_hour[5:7]

if meridiem == "AM":
    if hours == 12:
        hours = 00
elif meridiem == "PM":
    if hours != 12:
        hours += 12

print(f"{hours:02}:{minutes:02}")
