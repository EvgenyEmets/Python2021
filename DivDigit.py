def divdigit(N):
    counter = 0
    for i in range(1, 10):
        if N % i == 0:
            tmpn = N
            while tmpn > 0:
                comp = tmpn % 10
                if comp == i:
                    counter += 1
                tmpn //= 10
    return counter
