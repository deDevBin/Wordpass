import random
import os

nounlist = []
verblist = []
adjectivelist = []

print(os.getcwd)

n = os.getcwd() + r'\Wordpass\nouns.txt'
v = os.getcwd() + r'\Wordpass\verbs.txt'
a = os.getcwd() + r'\Wordpass\adjectives.txt'
f = os.getcwd() + r'\Wordpass\pass.txt'

with open (n, 'rt') as nouns:
    for nline in nouns:
        nounlist += [nline.split(',')[0]]

with open (v, 'rt') as verbs:
    for nline in verbs:
        verblist += [nline.split('\n')[0]]

with open (a, 'rt') as adjectives:
    for nline in adjectives:
        adjectivelist += [nline.split('\n')[0]]

x = nounlist[random.randint(0, len(nounlist))] + " " + verblist[random.randint(0, len(verblist))] + "s " + adjectivelist[random.randint(0, len(adjectivelist))] + " " + nounlist[random.randint(0, len(nounlist))]
print(x)

file = open(f, 'w')
file.write(x)
file.close()