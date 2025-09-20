from abc import ABC, abstractmethod

class Command(ABC):
    def __init__(self, flashlight):
        self.flashlight = flashlight

    @abstractmethod
    def execute(self):
        pass


class TurnLightOn(Command):
    def execute(self):
        self.flashlight.turn_on()


class TurnLightOff(Command):
    def execute(self):
        self.flashlight.turn_off()