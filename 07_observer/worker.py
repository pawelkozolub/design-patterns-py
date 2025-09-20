from observable import Observable
from random import randint

class Worker(Observable):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.progress = 0
        self.limit = 100
    
    def __str__(self):
        return self.name
    
    def do_work(self):
        self.progress += randint(1, 10)
        self.progress = self.limit if self.progress > self.limit else self.progress
        self.notify(self.progress)