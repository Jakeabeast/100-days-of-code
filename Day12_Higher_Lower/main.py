'''
DAY 12 PROJECT - Guessing Game

The goal of this project is to use create the game Higher or Lower
The game is simple, you need to guess number between 1-100 within a limited number of tries.
A false guess with tell you whether you need to guess higher or lower to get the target number.
'''

import art
from random import randint

def choose_difficulty():
    while True:
        ans = input("Choose \"easy\" or \"hard\" difficulty >> ").lower()
        if ans == "easy":
            return 10
        elif ans == "hard":
            return 5
        else:
            print(f"{ans} is not a valid choice.")

def guess_number():
    while True:
        try:                
            ans = int(input("Guess a number between 1 - 100 >> "))
            if ans > 1 and ans < 100:
                return ans
            else:
                print("Must be between 1 - 100 (not including 1 or 100).")
        except:
            print("Please only enter an integer.")

if __name__ == "__main__":

    print(art.logo)
    remaining_guesses = choose_difficulty()
    target_number = randint(2,99) #between 1 - 100 (not including)
    win = False
    while remaining_guesses > 0:
        print(f"You have {remaining_guesses} guesses remaining.")
        guess = guess_number()
        if guess < target_number:
            print("Too low.")
        elif guess > target_number:
            print("Too high.")
        else:
            win = True
            break
        remaining_guesses -= 1
    
    if win:
        print("YOU GUESSED THE NUMBER!")
    else:
        print("Bad luck, you've run out of guesses.\n" + \
             f"The correct number is {target_number}.")


