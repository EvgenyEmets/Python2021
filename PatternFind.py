s = input()
p = input().split("@")
pos = s.find(p[0])
while pos != -1:
    shift = pos
    for i in p:
        if s[shift:shift+len(i)] != i:
            pos = s.find(p[0], pos+1)
            break
        shift += len(i) + 1
    else:
        break
print(pos)
    
