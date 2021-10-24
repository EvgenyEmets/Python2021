from decimal import *
import math

def Pi():
    getcontext().prec += 400
    three = Decimal(3)
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n+na, na+8
        d, da = d+da, da+32
        t = (t * n) / d
        s += t
    getcontext().prec -= 400
    return +s

def Cos(x):
    getcontext().prec += 150
    i, lasts, s, fact, num, sign = 0, 0, 1, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 150
    return +s

def Sin(x):
    getcontext().prec += 150
    i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 150
    return +s


x = input()
p = int(input())
getcontext().prec = p
getcontext().prec += 150
pi = Pi()
x = Decimal(x)
x = x * pi / 200
s = Sin(x)
c = Cos(x)
getcontext().prec -= 150
print(s/c)
