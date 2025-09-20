# Series of subsequent natural number squares: 0, 1, 4, 9, 16, 25, ...

class MyIter:
    def __init__(self, limit):
        self.n = 0
        self.limit = limit
        self.add = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n < self.limit:
            self.n += self.add
            self.add += 2
            return self.n
        else:
            self.n = 0
            self.add = 1
            raise StopIteration