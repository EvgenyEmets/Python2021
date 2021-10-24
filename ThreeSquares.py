from math import sqrt, ceil

seq = list(eval(input()))
sseq = set(seq)
m = max(sseq) + 1
possible = set()
for i in range(1, ceil(sqrt(m))):
    for j in range(i, ceil(sqrt(m - i*i))):
        for k in range(j, ceil(sqrt(m - i * i - j * j))):
            possible.add(i*i+j*j+k*k)
ans = possible & sseq
print(len(ans))
