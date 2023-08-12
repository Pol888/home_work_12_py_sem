class Factorial_iterator:
    def __init__(self, start, stop=None, step=None):
        if stop == None and step == None:
            self.start = 1
            self.stop = start
            self.step = 1
        elif step == None:
            self.start = start
            self.stop = stop
            self.step = 1
        else:
            self.start = start
            self.stop = stop
            self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            self.start += self.step
            return self.start - self.step
        raise StopIteration

f = Factorial_iterator(5, 10, 2)

print(*f)



