from team_member import TeamMember

class President(TeamMember):

    def process(self, task):
        if "meet" in task:
            if "president" in task:
                self.meet_president()
                return True
            elif "minister" in task:
                self.meet_prime_minister()
                return True
        return False

    @staticmethod
    def meet_president():
        print("Meet a president.")

    @staticmethod
    def meet_prime_minister():
        print("Meet a prime minister.")