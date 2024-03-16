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
        self.current_result = "0"

        self.output()

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


    def input():
        pass

    def update():
        pass
    
    def output():
        pass


if __name__ == "__main__":
    calc = Calculator()

    while calc.calculating == True:
        calc.input()
        calc.update()
        calc.output()

    print("Goodbye")