class Command:
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self, data=""):
        print(f"Command delegated to reciever.")
        self._receiver.execute(data)