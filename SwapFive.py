num = int(input())
over = 0
nxtnum = num
res = 0
power = 1
while True:
    res += power * nxtnum
    power *= 10
    nxtnum *= num
    nxtnum += over
    over = nxtnum//10
    nxtnum %= 10
    if nxtnum == num and over == 0:
        break
print(res)
