from art import logo
from os import system

'''
DAY 10 PROJECT - Calculator

The goal of this project is to use create a calculator where the user can use an operation one step at a time. 
For this project and hopefully onwards, I wont to try dedicating more commits to smaller chunks of code.
This should help make it more clear what has been done and prepares me for future version control princples. 
P.S I feel I may have made unnecessary implementations such as using individual functions for basic operations ):
'''

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = { '+' : add,
               '-' : subtract,
               '*' : multiply,
               '/' : divide }


if __name__ == "__main__":
    exit = False
    while not exit:
        print(logo)
        result = float(input("What's the first number?: "))
        for symbol in operations:
            print(symbol)
        bing = True
        while bing == True:
            action = input("What's the operation?: ").strip()
            number = float(input("What's the next number?: "))

            new_result = operations[action](result, number)
            print(result, action, number, "=", new_result)   

            reoccur = None
            while reoccur == None:
                reoccur = input(f"Type \"y\" to continue calculating with {result}, type \"n\" to clear, or \"exit\" to close calculator: ").lower()
                
                if reoccur == 'y':
                    result = new_result
                    bing = True
                elif reoccur == 'n': 
                    bing = False
                    system('cls')
                elif reoccur == 'exit':
                    bing = False
                    exit = True
                else:
                    print(f"You cannot choose 'reoccur'.")
                    reoccur = None
            
    print("Goodbye.")