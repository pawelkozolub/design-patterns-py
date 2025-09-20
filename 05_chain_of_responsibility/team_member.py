from abc import ABC

class TeamMember(ABC):

    def process(self, task):
        print("No one can do it. Please hire a specialist.")