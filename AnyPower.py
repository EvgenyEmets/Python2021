num = int(input())
power = 2
countmin = 0
count = 0
while num > 1:
    if num%power == 0:
        num//=power
        count += 1
        continue
    elif count != 0:
        if count == 1:
            print("NO")
            break
        elif countmin > count:
            if countmin%count == 0:
                countmin = count
                count = 0
            else:
                print("NO")
                break
        elif countmin != 0:
            if count%countmin != 0:
                print("NO")
                break
            else:
                count = 0
        else:
            countmin = count
            count = 0
    power += 1
else:
    if countmin == 0 and count == 1:
        print("NO")
    else:
        print("YES")
