from team_member import TeamMember

class Manager(TeamMember):

    def process(self, task):
        if "find" in task:
            self.find_worker()
            return True
        if "task" in task:
            self.add_task()
            return True
        if "check" in task and "process" in task:
            self.check_process()
            return True
        return False
    
    @staticmethod
    def find_worker():
        print("Find a worker.")

    @staticmethod
    def add_task():
        print("Add task to a worker.")

    @staticmethod
    def check_process():
        print("Check the process.")