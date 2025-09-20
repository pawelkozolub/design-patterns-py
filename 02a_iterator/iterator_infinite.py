# Series of subsequent natural number squares: 0, 1, 4, 9, 16, 25, ...

class MyInfiniteIter:
    def __init__(self):
        self.n = 0
        self.add = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.n += self.add
        self.add += 2
        return self.n