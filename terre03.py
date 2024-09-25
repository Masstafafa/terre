import sys

letters = sys.argv[1:]

for letter in letters:
    print(letter)
    ascii_value = ord(letter)
    
for ascii_code in range(ascii_value, 123):
    print(chr(ascii_code), end='')
print()