from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    #Create instances of each class
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    #Show the menu to the user
    while True:
        print("Welcome to the Coffee Machine!")
        menu_options = menu.get_items()
        print(f"Available drinks: {menu_options}")
        
        #Ask the user to select a drink
        choice = input("What would you like to order? or 'off' to exit: ").lower()

        if choice == "off":
            print("Turning off the coffee machine. Goodbye!")
            break

        if choice == "report":
            coffee_maker.report()
            continue

        #Find the selected drink from the menu
        drink = menu.find_drink(choice)

        if drink:
            #Check if there are enough resources to make the drink
            if coffee_maker.is_resource_sufficient(drink):
                # Proceed to payment
                if money_machine.make_payment(drink.cost):
                    #Make the coffee
                    coffee_maker.make_coffee(drink)
                else:
                    print("Payment was not successful. Please try again.")
            else:
                print("Sorry, we cannot make that drink due to insufficient resources.")
                
if __name__ == "__main__":
    main()
