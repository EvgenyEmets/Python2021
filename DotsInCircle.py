x, y, r = eval(input())
r *= r
a, b = eval(input())
while (a, b) != (0, 0):
    if (a - x)**2 + (b - y)**2 > r:
        print("NO")
        break
    a, b = eval(input())
else:
    print("YES")
