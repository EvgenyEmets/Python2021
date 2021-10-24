a = input().split()
d = dict()
while len(a) == 2:
    if a[0] not in d:
        d[a[0]] = set()
    d[a[0]] |= {a[1]}
    if a[1] not in d:
        d[a[1]] = set()
    d[a[1]] |= {a[0]}
    a = input().split()
entry = a[0]
exit = input()
set1 = d[entry]
set2 = {entry}
set3 = d[entry]
dif = 0
while dif != len(set1):
    dif = len(set1)
    set1 = set1 | set2
    set2.clear()
    for i in set3:
        set2 = set2 | d[i]
    set3 = set2 - set1
if exit in set1:
    print("YES")
else:
    print("NO")
