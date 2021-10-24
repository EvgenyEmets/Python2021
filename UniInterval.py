a = eval(input())
b = list()
for i in a:
    b.append((i[0], -1))
    b.append((i[1], 1))
b.sort()
count = 0
length = 0
start = 0
for i in b:
    if i[1] == -1:
        count += 1
        if count == 1:
            start = i[0]
    else:
        count -= 1
        if count == 0:
            length += i[0] - start
print(length)
