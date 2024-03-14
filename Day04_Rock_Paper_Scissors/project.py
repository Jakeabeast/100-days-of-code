'''
DAY 4 PROJECT - Rock Paper Scissors

The goal of this project is to recreate the classic game Rock Paper Scissors.
It will use a random AI mechanism to generate the computers choice.
'''

#=========================================================================
import random

choices = ("rock", "paper", "scissors")

#rules = {{"rock", "rock"} : "tie", {"rock", "paper"} : "win"} dictionary of rules
'''
             |  Rock  |  Paper  | Scissors
    ---------+--------+---------+----------
    Rock     |  Tie   |   Loss  |   Win
    ---------+--------+---------+----------
    Paper    |  Win   |   Tie   |   Loss
    ---------+--------+---------+----------
    Scissors |  Loss  |   Win   |   Tie
    ---------+--------+---------+----------
'''

dominate = {"rock" : "scissors",
            "scissors" : "paper",
            "paper": "rock"}

rules = {}
for c1 in choices:
    for c2 in choices:
        if c1 == c2:
            rules[c1,c2] = ("tied", "tied")
        elif dominate[c1] == c2:
            rules[c1,c2] = ("won", "loss")
        else:
            rules[c1,c2] = ("loss", "won")

gesture = {"rock" : '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) 
''',
          "paper" : '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
          "scissors" : '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''}

running = True

# Pre Game Loop functions
def display_rules():
    print('''Welcome to Rock Paper Scissors!
             - ROCK smashes SCISSORS
             - SCISSORS cuts PAPER
             - PAPER wraps ROCK''')
    
#============================================================

# Input functions for player and AI
def player_selection():
    return input("Please select either \"rock\", \"paper\", or \"scissors\". Type \"exit\" to leave game. ").lower()
    
def AI_selection():
    return random.choice(choices)

#============================================================

#Update functions
def update(player, AI):
    if player == "exit": 
        global running
        running = False
        return ""
    
    if validate(player):
        ai_choice = AI()
        return ((player, ai_choice),(rules[player, ai_choice])) #returns nested tuple

    else:
        print("Invalid move. Please try again.")
        return ""
        

def validate(choice):
    return True if choice in choices else False

#============================================================

def render(result):
    if not result == "":
        print('='*5 + "Player Throws" + '='*5)
        print(gesture[result[0][0]])
        print('='*5 + "Computer Throws" + '='*5)
        print(gesture[result[0][1]])
        print(f"\nPlayer {result[1][0]}. Computer {result[1][1]}.\n")
    

#============================================================

# Main
if __name__ == '__main__':
    display_rules()

    while running is True:
        choice = player_selection()
        result = update(choice, AI_selection)
        render(result)

    print("Goodbye!")
