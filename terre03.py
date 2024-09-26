import sys

arguments = sys.argv[1:]
letter_ascii = ord(arguments[0])

   
for letter_ascii in range(letter_ascii, 123):
    print(chr(letter_ascii), end='')
print()