'''
introduction
'''

import time

class CoffeeMachine():

    MENU = {
        "espresso" : {
            "ingredients" : {
                "water" : 50,
                "milk" : 0,
                "coffee" : 18
            },
            "cost" : 1.5
        },
        "latte" : {
            "ingredients" : {
                "water" : 200,
                "milk" : 150,
                "coffee" : 24
            },
            "cost" : 2.5
        },
        "cappucino" : {
            "ingredients" : {
                "water" : 250,
                "milk" : 100,
                "coffee" : 24 
            },
            "cost" : 3.0
        }
    }

    def __init__(self):
        self.on = False
        self.water = 500
        self.milk = 300
        self.coffee = 100
        self.profit = 0
        
        self.user_coins = 0


    def __is_admin(self):
        if input("Are you an Admin? ('Y'\'N')\n").lower() == 'y':
            return True
        else: 
            return False 
        

    def __admin_selection(self):
        print("Options:\n- Order Coffee ('coffee')\n- Top up ingredients ('ingredients')\n" + \
                        "- Generate report ('report')\n- Turn off machine ('off')\n")
        while True:
            selection = input().lower()
            if selection == "coffee":
                self.__coffee_menu_selection()
            elif selection == "ingredients":
                self.__add_ingredients()
            elif selection == "report":
                self.__generate_report(admin=True)
            elif selection == "off": 
                self.on_off()
            else:
                print("Invalid selection. Try again.")
                continue
            break


    def __customer_selection(self):
        self.__coffee_menu_selection()


    def __coffee_menu_selection(self):
        while True:
            selection = input("What coffee would you like? ('espresso'/'latte'/'cappucino')").lower()
            
            if selection == "report":
                self.__generate_report()
            elif selection in ("espresso", "latte", "cappucino"):
                if self.__check_ingredients(selection) and self.__process_coins(selection):
                    self.__make_drink(selection)
                    self.__generate_report(admin = False)
            else:
                print("Invalid selection, try again?")
                continue
            break


    def __make_drink(self, drink):
        print("Making " + drink, end='')

        self.water -= self.MENU[drink]["ingredients"]["water"]
        self.milk -= self.MENU[drink]["ingredients"]["milk"]
        self.coffee -= self.MENU[drink]["ingredients"]["coffee"]

        for _ in range(3):
            time.sleep(1)
            print('. ', end='')
        time.sleep(1)
        print('!')
        print(f"Here is your {drink}. Enjoy!\n")


    def __generate_report(self, admin):
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee: {self.coffee}g")
        if admin:
            print(f"Money: ${self.profit}")
        print('\n')


    def __process_coins(self, drink):
        total = 0
        try:
            print("Please insert coins.")
            total += int(input("How many quarters >> ")) * 0.25 
            total += int(input("How many dimes >> ")) * 0.1
            total += int(input("How many nickles >> ")) * 0.05
            total += int(input("How many pennies >> ")) * 0.01
        except:
            print(f"There was an error with processing you're coins.\nReturning coins: ${total}.\n")
            return False

        cost = self.MENU[drink]["cost"]
        if total >= cost:
            self.profit += cost
            total -= cost
            print(f"Here is your remaining change: ${round(total, 2)}.\n")
            return True
        else:
            print(f"Sorry, that's not enough money. Money refunded: ${total}\n")
            return False


    def __check_ingredients(self, drink):
        if self.water < self.MENU[drink]["ingredients"]["water"]:
            print("Sorry, there is not enough water.")
            return False
        elif self.milk < self.MENU[drink]["ingredients"]["milk"]:
            print("Sorry, there is not enough milk.")
            return False
        elif self.coffee < self.MENU[drink]["ingredients"]["coffee"]:
            print("Sorry, there is not enough coffee.")
            return False
        else:
            return True
         

    def __add_ingredients(self):
        try:
            self.water += int(input("Enter water amount in millileters. "))
            self.milk += int(input("Enter milk amount in millileters. "))
            self.coffee += int(input("Enter coffee amount in millileters. "))
        except:
            print("Error with adding ingredient.")


    def on_off(self):
        self.on = not self.on


    def running(self):
        if self.__is_admin():
            self.__admin_selection()
        else:
            self.__customer_selection()        



if __name__ == "__main__":
    machine = CoffeeMachine()
    machine.on_off()

    power = True
    while power and machine.on:
        machine.running()
