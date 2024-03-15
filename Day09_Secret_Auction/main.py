'''
DAY 9 PROJECT - Secret Auction

The goal of this project is to use dictionaries to replicate a secret auction. 
It will act by havnig someone enter their name and price, wipe the data using OS shell commands, then repeat for the remaining people.
In the end the highest bidder is the winner.
'''

class Auction():
    def __init__(self):
        self.dict = {}
        self.auctioning = True

        self.name = None
        self.bid = None
        self.remaining_people = ''

        self.__welcome()

    def __welcome(self):
        from art import auction_hammer
        print(auction_hammer)
        print("Welcome to the secret auction program.")

    def __continue(self):
        self.remaining_people = input("Any other bidders? Type \"Yes\" or \"No\".").lower()

    def input(self):
        self.name = input("What is your name? >> ")
        try:
            self.bid = float(input("What is your bid? >> $"))
        except:
            self.bid = 0
            print("That's not a number, putting you're bid to $0 automatically")
        self.__continue()

    def update(self):
        from os import system
        if self.remaining_people == "yes":
            self.dict[self.name] = self.bid
            system('cls')    

        elif self.remaining_people == "no":
            self.dict[self.name] = self.bid
            system('cls')
            self.auctioning = False

        else:
            print("Please only type \"Yes\" or \"No\".")
            self.__continue()
            self.update()

    def highest_bidder(self):
        from art import auction_hammer
        print(auction_hammer)
        highest_bidder = max(self.dict, key=self.dict.get)
        print("Winner is %s with $%s as their bid!" % (highest_bidder, self.dict[highest_bidder]))

if __name__ == '__main__':
    program = Auction()

    while program.auctioning:
        program.input()
        program.update()

    program.highest_bidder()
    print("Goodbye!")