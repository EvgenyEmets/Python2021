from itertools import groupby

def LookSay():
    seq = [1,]
    while True:
        for i in seq:
            yield i
        tmp = []
        for i, j in groupby(seq):
            tmp.append(len(list(j)))
            tmp.append(i)
        seq = tmp
