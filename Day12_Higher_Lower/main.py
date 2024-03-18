'''
DAY 12 PROJECT - Guessing Game

The goal of this project is to use create the game Higher or Lower
The game is simple, you need to guess number between 1-100 within a limited number of tries.
A false guess with tell you whether you need to guess higher or lower to get the target number.
'''

import art


def choose_difficulty():
    while True:
        ans = input("Choose \"easy\" or \"hard\" difficulty >> ").lower()
        if ans == "easy":
            return 10
        elif ans == "hard":
            return 5
        else:
            print(f"{ans} is not a valid choice.")

if __name__ == "__main__":

    print(art.logo)
    remaining_guesses = choose_difficulty()
    while remaining_guesses > 0:
        print(remaining_guesses)

        remaining_guesses -= 1

    print("Game Over!")