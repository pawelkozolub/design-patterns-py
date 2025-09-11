from team_member import TeamMember

class Secretary(TeamMember):

    def process(self, task):
        if "call" in task:
            self.call()
            return True
        if "write" in task and "back" in task:
            self.write_back()
            return True
        return False
    
    @staticmethod
    def call():
        print("Make a call.")

    @staticmethod
    def write_back():
        print("Write back to a message.")