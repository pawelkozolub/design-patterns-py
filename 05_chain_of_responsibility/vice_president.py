from team_member import TeamMember

class VicePresident(TeamMember):

    def process(self, task):
        if "meet" in task:
            self.meet_others()
            return True
        if "sign" in task:
            self.sign_document()
            return True
        return False

    @staticmethod
    def meet_others():
        print("Meet a customer/team member/investor.")

    @staticmethod
    def sign_document():
        print("Sign a document.")