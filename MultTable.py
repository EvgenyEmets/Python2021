N, M = eval(input())
n = int(len(str(N)))
n1 = int(len(str(N*N)))
w = n + 3 + n + 3 + n1 + 3
col = M // w + (1 if M % w - w + 3 > 0 else 0) 
row = N // col + (1 if N%col else 0)
for i in range(row):
    print("="*M)
    for k in range(N):
        s = ""
        for j in range(col):
            if i*col+j+1 <= N:
                if j == 0:
                    tmp = f"{(i*col+j+1):{n}} * {k+1:<{n}} = {(i*col+j+1)*(k+1):<{n1}}"
                else:
                    tmp = f" | {(i*col+j+1):{n}} * {k+1:<{n}} = {(i*col+j+1)*(k+1):<{n1}}"
                s+= tmp
        print(s[:M])
print("="*M)
