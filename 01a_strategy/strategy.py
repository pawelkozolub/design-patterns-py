from abc import ABC, abstractmethod


class Strategy(ABC):
    def __init__(self):
        self.price = None
        self.velocity = None
        self.max_distance = None
        self.start_place = None

    @abstractmethod
    def goto(self, place):
        pass