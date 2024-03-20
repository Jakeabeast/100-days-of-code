'''
DAY 14 PROJECT - Highest Search Game

The goal of this project is to use recreate the game similar to HigherLower (https://www.higherlowergame.com/)
Ironically, this is also the name I called Day 12's project, however, it works differently.
In this game, you will be given a 2 people, their profession, the country they reside.
You must guess which person has a higher follower count to score points, else the game ends.
'''
import os

import art
import game_data

def random_compare():
    dataA, dataB = game_data.get_random_data()
    print(f"Compare A: {dataA['name']}, a {dataA['description']}, from {dataA['country']}.")
    print(art.vs)
    print(f"Against B: {dataB['name']}, a {dataB['description']}, from {dataB['country']}.")
    return dataA["follower_count"], dataB["follower_count"]

def player_input():
    ans = input("Who has more followers? Type 'A' or 'B': ").lower()
    if ans == 'a':
        return True
    elif ans == 'b':
        return False
    else:
        return None

if __name__ == "__main__":

    score = 0
    alive = True
    while alive:
        print(art.logo)
        if score > 0:
            print("You're right! Current score : %i." % score)

        a_count, b_count = random_compare()
        option_a = player_input()
        if option_a == None:
            alive = False
        elif a_count > b_count:
            if option_a:
                score += 1
            else:
                alive = False
        elif b_count > a_count:
            if not option_a:
                score += 1
            else: 
                alive = False
        else: 
            #if tie, give win
            score += 1 

        os.system('cls')
    
    print(art.logo)
    print("Sorry, that's wrong. Final score: %i." % score)
