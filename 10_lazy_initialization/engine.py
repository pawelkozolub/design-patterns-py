import time

class Engine:
    def __init__(self, type_):
        if type_ == "gasoline":
            time.sleep(5)
        elif type_ == "diesel":
            time.sleep(10)
        else:
            time.sleep(4)
        print("Engine created.")