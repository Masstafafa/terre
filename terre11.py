import sys
import re

arguments = sys.argv[1:]

if len(arguments) != 1:
    print("Erreur : Un seul argument doit être rentré,"
          " Merci d'indiquer l'horaire avec le format xx:xx")
    sys.exit()

full_hour = arguments[0]

time_regex = "^(2[0-4]|1[0-9]|0?[0-9]):([0-5][0-9])$"

if not re.match(time_regex, full_hour):
    print("Erreur : l'heure ne peut être comprise qu'entre O et 24"
          " les minutes ne peuvent être comprise qu'entre O et 59")
    sys.exit()

hours, minutes = map(int, full_hour.split(":"))

meridiem = "AM"
if hours > 12:
    hours -= 12
    meridiem = "PM"
elif hours == 12:
    meridiem = "PM"
elif hours == 0:
    hours = 12
print(f"{hours:02}:{minutes:02}{meridiem}")