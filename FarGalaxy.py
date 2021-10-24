a = input().split()
d = dict()
i = 0
while len(a) != 1:
    a[0] = float(a[0])
    a[1] = float(a[1])
    a[2] = float(a[2])
    d[a[3] + " " + str(i)] = (a[0], a[1], a[2])
    i += 1
    a = input().split()
c = d.keys()
c = sorted(c)
maxd = 0
farg = ["",""]
for i in range(len(c)):
    for j in range(i, len(c)):
        dist = (d[c[i]][0]-d[c[j]][0])**2+(d[c[i]][1]-d[c[j]][1])**2+(d[c[i]][2]-d[c[j]][2])**2
        if dist > maxd:
            maxd = dist
            farg = [c[i].split()[0], c[j].split()[0]]
print(*farg)
