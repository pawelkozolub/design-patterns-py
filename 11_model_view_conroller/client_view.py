import time

class ClientView:
    def show(self, meal):
        if meal is not None:
            print(f"Here is my {meal} meal.")
        else:
            print("There is no that meal.")
        time.sleep(3)

    def request_meal(self):
        return input("\nPut here the name of a meal: ")
    
    def show_menu(self, menu):
        for row in menu:
            print(row)