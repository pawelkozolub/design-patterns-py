from menu_model import MenuModel
from client_view import ClientView

class WaiterController:
    def __init__(self):
        self.menu = MenuModel()
        self.client = ClientView()

    def run(self):
        self.client.show_menu(self.menu.get_menu())
        valid_request = False
        name = ""
        
        while not valid_request:
            name = self.client.request_meal()
            if len(name) > 2:
                valid_request = True
        
        meal = self.menu.get_meal(name)
        self.client.show(meal)