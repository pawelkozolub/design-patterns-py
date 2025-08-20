from abc import ABC, abstractmethod


class Worker(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def prepare_to_work(self):
        pass

    @abstractmethod
    def go_to_work(self):
        pass

    def log_in(self):
        print(f"Logged in as {self.name}")

    @abstractmethod
    def start_work(self):
        pass
    
    @staticmethod
    def make_tea():
        print("Tea is made.")

    @abstractmethod
    def do_work(self):
        pass

    @abstractmethod
    def finish_work(self):
        pass

    @staticmethod
    def get_lunch():
        print("Lunch got.")

    # Template method
    def work_day(self):
        self.prepare_to_work()
        self.go_to_work()
        self.log_in()
        self.start_work()
        self.make_tea()
        self.do_work()
        self.get_lunch()
        self.do_work()
        self.finish_work()