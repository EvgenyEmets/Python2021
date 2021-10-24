def squares(w,h,*S):
    a = [["." for i in range(w)] for i in range(h)]
    for i in S:
        for x in range(i[0], i[0]+i[2]):
            for y in range(i[1], i[1]+i[2]):
                a[y][x] = i[3]
    for i in a:
        print(*i, sep = "")
