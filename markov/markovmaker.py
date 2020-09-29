import markovgen
import re
import string

original = open('twain.txt')
outfile = open('twain_markov.txt', 'w')

newtext = []
mk = markovgen.Markov(original)
counter = 0

while counter < 100:
    line = '\n' + mk.generate_markov_text()

    exclude = ['"', '(', ')', ';']
    line = ''.join(ch for ch in line if ch not in exclude)

    line = line.lower() + "."
    print(line)
    newtext.append(line)
    counter = counter + 1

for aline in newtext:
    outfile.write(aline)

outfile.close()
original.close()