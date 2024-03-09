'''
DAY 3 PROJECT - Choose Your Own Adventure

The goal of this project is to create a pathway based text adventure using conditional statements
'''

#=========================================================================

def decision(choices, prompt):
    # full_prompt == f"\n{prompt} Type \"{choice1}\" or \"{choice2}\". "
    full_prompt = prompt + " Type "
    selection = '"' + choices[0] + '"'

    for choice in choices[1:]:
        selection += " or \"" + choice + "\""
    selection += ". "
    full_prompt += selection

    c = input(full_prompt).lower()
    while not (c in choices):
        c = input(f"Must choose between " + selection)
    return c


print('''*******************************************************************************
                |                   |                  |                     |
        _________|________________.=""_;=.______________|_____________________|_______
        |                   |  ,-"_,=""     `"=.|                  |
        |___________________|__"=._o`"-._        `"=.______________|___________________
                |                `"=._o`"=._      _`"=._                     |
        _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
        |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
        |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
        _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
        |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
        |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
        ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
        /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
        ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
        /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
        ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
        /______/______/______/______/______/______/______/______/______/______/______/_
        *******************************************************************************''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
choice = decision(("left", "right"), "You're at a crossroad. Where do you want to go?")
if choice == "right":
    print("Fall into a hole.\nGame Over.")
    quit()

choice = decision(("wait", "swim", "jump in"), "You've come to a lake. There is an island in the middle of the lake.\nDo you wait for a boat or swim across?")
if not choice == "wait":
    print("Attack by trout.\nGame Over.")
    quit()
else: print("Hurry, Dex greets you on the other side.")
