def BinPow(a, N, f):
    if N > 2:
        if N % 2 == 0:
            bp = BinPow(a, N / 2, f)
            return f(bp, bp)
        else:
            return f(a, BinPow(a, N - 1, f))
    elif N == 1:
        return a
    elif N == 2:
        return f(a, a)
