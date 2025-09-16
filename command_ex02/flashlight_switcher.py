from command import TurnLightOn, TurnLightOff

class FlashlightSwitcher:
    def __init__(self, flashlight, switch):
        self._flashlight = flashlight
        self._switch = switch

    def toggle(self, command: str):
        if command.lower() == "on":
            self._switch.execute(TurnLightOn(self._flashlight))
        else:
            self._switch.execute(TurnLightOff(self._flashlight))