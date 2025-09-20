from strategy import Strategy


class Walk(Strategy):
    def __init__(self):
        super().__init__()
        self.price = 0
        self.velocity = 5
        self.max_distance = 25

    def goto(self, place):
        print(f"I went to place {place}.")


class Car(Strategy):
    def __init__(self):
        super().__init__()
        self.price = 4
        self.velocity = 60
        self.max_distance = 400

    def goto(self, place):
        print(f"I drove to place {place}.")


class Plane(Strategy):
    def __init__(self):
        super().__init__()
        self.price = 10
        self.velocity = 700
        self.max_distance = 10000

    def goto(self, place):
        print(f"I flew to place {place}.")