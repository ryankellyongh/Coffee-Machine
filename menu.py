class MenuItem:
    """ Models each Menu Item.""" 
    def __init__(self, name, water, milk, coffee,cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water":water, 
            "milk": milk, 
            "coffee":coffee
        }
        
class Menu:
    """ Models the Menu with drinks."""
    def __init__(self):
        self.menu =[ 
            MenuItem (name ="latte",water = 200, milk = 150,coffee= 24, cost=1),
            MenuItem (name ="cappucino",water = 200, milk = 150,coffee= 24, cost=1),
            MenuItem (name ="espresso",water = 200, milk = 150,coffee= 24, cost=1),]
            #add 3 menu i.e espresso, latte, cappuccino using menuitem class ]
        
    def get_items(self):
        """ returns all the names of the available menu items. """
        
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options
    
    def find_drink(self,order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
        return None