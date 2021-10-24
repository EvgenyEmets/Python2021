import random
import sys
L = int(input())
Txt = sys.stdin.read().replace("\n    ", " @ ").split()
d = dict()
for i in range(len(Txt) - 2):
    if (Txt[i], Txt[i+1]) not in d:
        d[(Txt[i], Txt[i+1])] = set()
    d[(Txt[i], Txt[i+1])].add(Txt[i+2])
random.seed()
a = random.randint(0,len(Txt)-L-1)

agr = ["" for i in range(L)]
agr[0] = Txt[a]
agr[1] = Txt[a+1]
for i in range(2,L):
    c = list(d[(agr[i-2], agr[i-1])])
    agr[i] = c[random.randint(0, len(c)-1)]
print(" ".join(agr).replace("@", "\n    "))
