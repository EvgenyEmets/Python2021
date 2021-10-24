pointer = 0
i, j = 0, 0
direction = 0
m, n = eval(input())
a = [[-1 for k in range(m)] for k in range(n)]
for k in range(n*m):
    a[i][j] = pointer
    pointer = (pointer + 1) % 10
    if direction == 0:
        j += 1
        if j == m or a[i][j] != -1:
            j -= 1
            i += 1
            direction = 1
    elif direction == 1:
        i += 1
        if i == n or a[i][j] != -1:
            i -= 1
            j -= 1
            direction = 2
    elif direction == 2:
        j -= 1
        if j == -1 or a[i][j] != -1:
            j += 1
            i -= 1
            direction = 3
    else:
        i -= 1
        if i == -1 or a[i][j] != -1:
            j += 1
            i += 1
            direction = 0
for k in a:
    print(*k)
