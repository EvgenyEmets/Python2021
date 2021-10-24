def det(a):
    if len(a) == 1:
        return a[0][0]
    else:
        agregate = 0
        for i in range(len(a)):
            sa = [[0 for i in range(len(a) - 1)] for j in range(len(a) - 1)]
            for j in range(1, len(a)):
                for k in range(0, i):
                    sa[j-1][k] = a[j][k]
                for k in range(i+1, len(a)):
                    sa[j-1][k-1] = a[j][k]
            agregate += a[0][i] * ((-1) ** (i)) * det(sa)
        return agregate


a = eval(input())
print(det(a))
