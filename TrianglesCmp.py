from math import sqrt

class Triangle:
    edge = [0, 0, 0]
    sq = 0
    def __init__(self, a, b, c):
        self.edge = [0, 0, 0]
        self.edge[0] = float(a)
        self.edge[1] = float(b)
        self.edge[2] = float(c)
        if max(a, b, c) * 2 >= a + b + c or min(a, b, c) <= 0:
            pass
        else:
            p = (a + b + c) / 2
            self.sq = sqrt(p * (p - a) * (p - b) * (p - c))

    def __str__(self):
        return str(self.edge[0]) + ":" + str(self.edge[1]) + ":" + str(self.edge[2])

    def __eq__(self, other):
        e1, e2 = sorted(self.edge), sorted(other.edge)
        return e1 == e2
    
    def __ge__(self, other):
        return self.sq >= other.sq
    
    def __lt__(self, other):
        return self.sq < other.sq
    def __bool__(self):
        return self.sq != 0
        

def abs(obj):
    return obj.sq
