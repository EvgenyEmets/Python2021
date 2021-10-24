num = int(input())
tmp = num
revnum = 0
while tmp > 0:
    revnum *= 10
    revnum += tmp%10
    tmp //= 10
if revnum == num:
    print("YES")
else:
    print("NO")
