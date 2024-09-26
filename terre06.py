
import sys

arguments = sys.argv[1:]

if len(arguments) == 0:
    print("Seul les mots ou chiffres entre guillemets sont pris en compte")
    sys.exit()

words = arguments[0]
reversed_words = ''

for letter in range(len(words) - 1, -1, -1):
    reversed_words += words[letter]
print(reversed_words)

#ou
#for letter in words:
#   reversed_words = letter + reversed_words
#print(reversed_words)

#python3 terre06.py 'test'