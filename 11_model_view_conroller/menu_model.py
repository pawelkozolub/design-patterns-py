import csv

class MenuModel:
    def __init__(self):
        self.file = "11_model_view_conroller/menu.csv"
        self.temp_menu = csv.DictReader(open(self.file, encoding="UTF-8"))
        self.menu = []
        for row in self.temp_menu:
            dictionary = dict()
            dictionary["Name"] = row["Name"]
            dictionary["Price"] = row["Price"]
            dictionary["Quantity"] = row["Quantity"]
            dictionary["Availability"] = row["Availability"]
            self.menu.append(dictionary)

    def get_meal(self, name):
        meal_exist = False
        meal_available = False
        for row in self.menu:
            if row["Name"] == name:
                meal_exist = True
                meal_available = int(row["Availability"])
        
        if meal_exist and meal_available:
            return name
        else:
            return None
        
    def get_menu(self):
        menu_to_return = []
        for row in self.menu:
            menu_to_return.append((row["Name"], row["Quantity"], row["Price"]))
        return menu_to_return