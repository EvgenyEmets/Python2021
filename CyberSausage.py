from fractions import Fraction
from math import floor

class Sausage:
    inner = "pork!"
    v = Fraction(1)
    def __init__(self, inner = "pork!", v = Fraction(1, 1)):
        self.inner = inner
        self.v = Fraction(v)
    def __add__(self, other):
        return Sausage(self.inner, self.v + other.v)
    def __sub__(self, other):
        if self.v < other.v:
            return Sausage(self.inner, Fraction(0))
        else:
            return Sausage(self.inner, self.v - other.v)
    def __mul__(self, other):
        return Sausage(self.inner, self.v*other)
    def __rmul__(self, other):
        return Sausage(self.inner, self.v*other)
    def __truediv__(self, other):
        return Sausage(self.inner, self.v/other)
    def __abs__(self):
        return self.v
    def __bool__(self):
        return self.v != 0
    def __str__(self):
        a = ["", "", "", "", ""]
        sticks = 0
        sticks = floor(self.v)
        for i in range(sticks):
            a[0] += ("/"+"-"*12+"\\")
            a[1] += ("|"+(self.inner*12)[:12]+"|")
            a[2] += ("|"+(self.inner*12)[:12]+"|")
            a[3] += ("|"+(self.inner*12)[:12]+"|")
            a[4] += ("\\"+"-"*12+"/")
        tail = floor(12 * (self.v - sticks))
        if sticks == 0 or tail != 0:
            a[0] += ("/"+"-"*tail+"|")
            a[1] += ("|"+(self.inner*tail)[:tail]+"|")
            a[2] += ("|"+(self.inner*tail)[:tail]+"|")
            a[3] += ("|"+(self.inner*tail)[:tail]+"|")
            a[4] +=("\\"+"-"*tail+"|")
        return "\n".join(a)
