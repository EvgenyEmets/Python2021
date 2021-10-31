from itertools import islice

def joinseq(*seq):
    iterlist = [islice(i, None) for i in seq]
    trylist = [next(i) for i in iterlist]
    active = len(seq)
    while active > 0:
        nxt = min(trylist)
        yield nxt
        ind = trylist.index(nxt)
        nxtins = next(iterlist[ind], None)
        if nxtins == None:
            trylist.pop(ind)
            iterlist.pop(ind)
            active -= 1
        else:
            trylist[ind] = nxtins
