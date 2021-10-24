a = list()
a.append(list(input()))
a.append(list(input()))
while a[-1][0] != "-":
    a.append(list(input()))
ans = 0
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] == "#" and a[i-1][j] != "#" and a[i][j-1] != "#":
            ans += 1
print(ans)
