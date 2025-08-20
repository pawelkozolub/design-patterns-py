from worker import Worker


class Analyst(Worker):
    def prepare_to_work(self):
        print("Prepare to work as an analyst.")

    def go_to_work(self):
        print("Go to an analyst office.")

    def log_in(self):
        print(f"Log in as an analyst: {self.name}")

    def start_work(self):
        print(f"Start analyst task for a day assigned to {self.name}.")

    def do_work(self):
        print("Do an analyst work.")

    def finish_work(self):
        print("Finish analyst tasks for today.")