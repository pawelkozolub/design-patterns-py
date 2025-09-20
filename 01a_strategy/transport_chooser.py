import sys, inspect
from random import choice
from typing import Optional, Type
from strategy import Strategy
from strategies import *


class TransportChooser():
    def __init__(self, destination, strategy: Optional[Strategy]=None):
        self.strategy = strategy
        self.destination = destination
        
        # Collect only concrete subclass of Strategy abstract class
        self.strategies: list[Type[Strategy]] = [
            cls for _, cls in inspect.getmembers(sys.modules["strategies"], inspect.isclass)
            if issubclass(cls, Strategy) and cls is not Strategy
        ]
        
    def use_strategy(self):
        if not self.strategy:
            chosen_cls = choice(self.strategies)
            print(f"Applying strategy: {chosen_cls.__name__}")
            self.strategy = chosen_cls()
        self.strategy.goto(self.destination)