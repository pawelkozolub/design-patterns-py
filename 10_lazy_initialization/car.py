from datetime import datetime
from engine import Engine

class Car:
    def __init__(self, model, engine_type):
        self.model = model
        self.engine_type = engine_type
        self.engine = None
        self.year = datetime.now().year

    def take_a_look(self, observer):
        print(f"{observer} is taking a look into {self.model}.")

    def request_additional_information(self):
        print(f"It is {self.model} from {self.year} year. "
              f"It has a {self.engine_type} engine type.")
        
    def test_drive(self, observer):
        if self.engine is None:
            self.engine = Engine(self.engine_type)
        print(f"{observer} is testing the {self.model} car...")