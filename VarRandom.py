from random import randint

def randomes(seq):
    #seq = [list(i) for i in seq]
    seq1 = list()
    flg = True
    flg2 = False
    while True:
        for i in seq:
            if flg and hasattr(i, "__next__"):
                seq1.append(list(i))
                for j in seq:
                    seq1.append(list(j))
                flg = False
                seq = seq1
                break
            yield randint(i[0], i[1])
