import sys

choice_letter = sys.argv[1]

for letter in range(ord(choice_letter), ord('z') + 1):
    print(chr(letter), end='')

print()
        
