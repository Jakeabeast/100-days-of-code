from art import logo

'''
DAY 10 PROJECT - Calculator

The goal of this project is to use create a calculator where the user can use an operation one step at a time. 
For this project and hopefully onwards, I wont to try dedicating more commits to smaller chunks of code.
This should help make it more clear what has been done and prepares me for future version control princples. 
P.S I feel I may have made unnecessary implementations such as using individual functions for basic operations ):
'''

class Calculator():

    def __init__(self):
        self.calculating = True
        self.current_result = None
        self.operation = None
        self.number = None
        

        self.options = { '+' : self.__add,
                         '-' : self.__subtract,
                         '*' : self.__multiply,
                         '/' : self.__divide }
        print(logo)

    def __add(self, number):
        return self.current_result + number

    def __subtract(self, number):
        return self.current_result - number

    def __multiply(self, number):
        return self.current_result * number

    def __divide(self, number):
        return self.current_result / number
    
    def __reset(self):
        from time import sleep
        from os import system
        self.current_result = None
        print("Resetting.")
        sleep(1)
        system('cls')
        print(logo)


    def input(self):
        if self.current_result == None:
            self.current_result = input("What's the first number: ")
            for symbol in self.options:
                print(symbol)            

        self.operation = input("Pick and operation: ")
        self.number = input("Pick the next number: ")

    def update(self):
        pass




if __name__ == "__main__":
    calc = Calculator()

    while calc.calculating == True:
        calc.input()
        calc.update()

    print("Goodbye")