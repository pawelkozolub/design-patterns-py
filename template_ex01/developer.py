from worker import Worker


class Developer(Worker):
    def prepare_to_work(self):
        print("Prepare to work as a developer.")

    def go_to_work(self):
        print("Go to a developer office.")

    def log_in(self):
        print(f"Log in as a developer: {self.name}")

    def start_work(self):
        print(f"Start developer tasks for a day assigned to {self.name}.")
    
    def do_work(self):
        print("Do a developer work.")

    def finish_work(self):
        print("Finish developer tasks for today.")