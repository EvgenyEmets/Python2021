class Dots:
    start = 0
    end = 0
    iterator = 0
    def __init__(self, a, b):
        self.start = a
        self.end = b
    def gen(s1, s2, inter):
        for i in range(s1, s2):
            yield self.start + i * self.inter
    def __getitem__(self, key):
        if str(type(key)) == "<class 'slice'>":
            start = key.start
            stop = key.stop
            step = key.step
        else:
            start = None
            stop = key
            step = None
        if not (step == None):
            if  stop == None:
                stop = step
            else:
                step, stop = stop, step
        inter = (self.end - self.start) / (stop - 1)
        if start == None and step == None:
            return gen(0, stop, inter, self.start)
        elif step == None:
            return self.start + start * inter
        elif start == None:
            return gen(0, step, inter, self.start)
            """
            for i in range(0, step):
                yield self.start + i * inter
            """
        else:
            return gen(start, step, inter, self.start)
            """
            for i in range(start, step):
                yield self.start + i * inter
            """

def gen(s1, s2, inter, start):
    for i in range(s1, s2):
        yield start + i * inter
