class Flashlight:
    def __init__(self, state="off"):
        self.state = state

    def turn_on(self):
        print("Flashlight is turned on")
        self.state = "on"

    def turn_off(self):
        print("Flashlight is turned off")
        self.state = "off"