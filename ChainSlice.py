from itertools import *

def chainslice(s, e, *seq):
    for i in list(islice(chain.from_iterable(seq), s, e)):
        yield i
