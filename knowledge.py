'''
Just for clarification, this knowledge.py files will be used to store ideas and featrures that I explored.
The structure will be a day by day basis.
I will use folding to fold up each day with a summary of what there is within that section

'''

#Instant variable swap | Code intelligence | Reuse specific function from imported library | Aliasing library
#Day01
#===============================================================

#1 - VARIABLE SWAP
a = 2
b = 7

#we could create a temporary variable to swap as such
tmp = a
a = b
b = a

#or we can do a single line instant swap with python
a, b = b, a

#===============================================================

#2 - CODE INTELLIGENCE
#intellisense, code intelligence or linting

#===============================================================

#3 - SPECIFIC FUNCTIONS FROM LIBRARIES
# I attempted to bypass a flawed test case using the random library to succeed the only two test cases
import random
random.randint(3, 8) # 3,4,5,6,7,or 8 

#decided to test using from keyword to extract specific function randint
from random import randint
randint(1,2) # 1 or 2

#===============================================================

#4 LIBRARY ALIASING

import random as urmom
urmom.randint(69)

#===============================================================

#Interpolation operator (string formatting)| Line shift and duplication | Manual fold | Rounding float
#Day02
#===============================================================

#1 - INTERPOLATION OPERATOR (string formatting w %)
two_digit_number = input()
num1 = int(two_digit_number[0])
num2 = int(two_digit_number[1])

print("%i + %i = %i" % (num1, num2, num1 + num2))
#output : 3 + 9 = 12

#make sure that after string we follow with % and (val1, val2)
#brakets aren't needed for a single value however.

print('%(language)s has %(number)03d quote types.' % {'language': "Python", "number": 2})
#output: Python has 002 quote types.
#neat addition of using dictionary with string formatting and how to use %d to add 0 spacing

#===============================================================

#2 - (SHIFT) + ALT + ARROW KEY
#ALT + ARROW: takes a line and moves it up or down throughout the code
#SHIFT + ALT + ARROW: takes a line and duplicates it up or down
#SHIFT + ALT + ARROW: takes a line and duplicates it up or down

#===============================================================

#3 - ADDING MANUAL FOLDS TO CODE
#(CTRL + K) -> (CTRL + ,) - Adds fold for selected region
#(CTRL + K) -> (CTRL + .) - Removes folds throughout selected region

#===============================================================

#4 - ROUND FLOAT DOWN TO INTEGER
num = 8 / 3 # = 2.6666666667 (float)

#--- USE THIS FOR NORMAL ROUNDING ---#
round(num) # = 3 
round(num, 3) # = 2.667

#--- USE THIS FOR ALWAYS ROUNDING DOWN ---#
num//1 # = 2 (int) # Using // simply divdeds by number then ignores all decimals (2.667/1 -> 2.0) or (8//3 -> 2)

#--- ALTENATIVELY USE FLOOR AND CEIL ---#
from math import floor, ceil
floor(num)
ceil(num) #rounded_up_answer = num//1 if num % 1 == 0 else (num + 1)//1 [solution without math library]

#===============================================================

#Tenary operator (conditional statement with result), ASCCI art, Commenting shortcut
#Day03

#===============================================================

#1 - TERNARY OPERATOR
num = 5
result = "even" if num % 2 == 0 else "odd" #stores "even" or "odd" in result

print ("Both a and b are equal" if a == b else "a is greater than b"
        if a > b else "b is greater than a") #for multiple conditions (no elif)

a, b = 7, 4
print ((a,"is greater.") if a > b else (b,"is greater!"))

#===============================================================

#2 - ASCII ART
#https://ascii.co.uk/art

print("""                       /|                 |\
                      / | ___.--~~~--.___ | \
 ...--=.._           /  ~~___~\_   _/~___~~  \        _..=--...
~   .-=_)/==._     _ \ .(~  o~-.\ /.-~o  ~). / _  _.==\(_=-.   ~~-._
  _/.-  /         / \/\_ ~---~_-=V=-_~---~ _/\/ \      \  -.\_      -
 /_/  ./          \/\_-_~~v-/~o~) (~o~\-v~~_-_/\/       \.  \_\      ~
//    |          _-=___==/(__         __)\==___=-_       |    \\\
 ))    \          _/ _ \ X___---===---___X / _ \_       /    (( ))\
\ \_   |         /_\/_\ (( \| ` ` ' ' |/ )) /_\/_\      |   _/ /|  \
 \  \   \       ~~  / _ /\\ V  /~V~)  V //\ _ \  ~~    /   /  / |   \
  \_ \  |           \/ \\ \\^  \ )/   ^//|// \/        |  / _/  |    \
    \ \  \               '/\\^  )/   ^// |`           /  / /     |
     \ \_ |             '| (\\^ V   ^//  |`          | _/ /      |
      \  \\             '/(~~\`-___-'/) /`           //  /       |
       \_ \\ /|        '|(~~~-\_   _/)  |`          |\ _/        |
         \_/~~~~-.     '/(~~~---===~~)  |`      .-~~~~~\_       |
._      _/   _    \   '|(~~~-----~~~)  /`      /     _   \_ .-. | _._
  \    // / /\\~)  \  '|(~~~-----~~~)  |`     /   (~//\ \ \X   \|/   \
------/ \ \ )--=====----=====------------=====-----===-\_) \\---------
      \ (\_)\                                            /\_)\
       \_)\                                                /\_)
        \                                                    /""")

#==============================================================

#3 - Comment Out shortcut
# select multiple lines and use (CTRL + /) to comment them in or out

#==============================================================


#Split string function | Find index of specific element | Random choice from list of items | Parsing random functions as object arguments 
#Day04

#===============================================================

#1 - SPLIT FUNCTION
str = "Angela, Ben, Jenny, Michael, Chloe"
names = str.split(", ") #list of names

#we can split a string with a custom seperator (", ")

#===============================================================

#2 - FIRST ELEMENT INDEX
letters = ['A', 'B', 'B', 'A']
posA = letters.index('A') #return index 0

#===============================================================

#3 - RANDOM FROM LIST
chosen_list = {"rock", "paper", "scissors"}
rand = random.randint(1,3)
result = "rock" if rand == 1 else "paper" if rand == 2 else "scissors"
#instead
result = random.choice(chosen_list)

#===============================================================

#4 - PARSING FUNCTION OBJECTS AS ARGUMENTS
def AI_selection():
    return random.choice(chosen_list)
def Bias_AI_selection():
    return "scissors"


def update(function):
    return function()

update(AI_selection) #choosen function (AI_selection) will be called as (function()) in update function
update(Bias_AI_selection) #or even Bias

#FUTHERMORE - We can parse random functions within a list for varying behaviours

func_list = [AI_selection, Bias_AI_selection]
update(func_list(random.randint(0,1))) #store functions as objects then randomly select function to use in update

#===============================================================

#Range without idx | Unique random values from list | Line/code structure maniuplation | Convert list to string
#Day05

#========================================================

#1 - RANGE LOOP WITHOUT IDX
#normally
for x in range(1, 11):
    print("blah") #wastes storage of x (not needed)

#instead
    for _ in range(1,11):
        print("yaay") #underscore bleeps out x when not needed

#========================================================
  
#2 - UNIQUE RANDOM VALUES FROM LIST
list = ["apple", "banana", "cherry", "Mango"]
random_unique = random.sample(list, 3) #random list of 3 fruits (never does apple twice)

#========================================================

#3 - LINE/CODE STRUCTURE MANIPULATION
list = ["apple" , "banana" \
        "cherry", "Mango"] #Use (\) to continue line below

num1 = 7; num2 = 27 #use (;) to use same line for multple things.

#========================================================

#4 - CONVERT LIST TO STRING
list = ["apple", "banana", "cherry", "Mango"]
print(', '.join(list)) #"apple, banana,..."

#========================================================

#Nothing
#Day06

#Importing libraries | Clearing terminal screen using OS
#Day07
#========================================================

#1 - IMPORTING
#We can import multiple specific items on the same line. Also . to travel through relative folder path.
from Day07_Hangman.hangman_art import logo, stages

#========================================================

# 2 - CLEAR SCREEN USING OS 

import os
def clear():
    #opens the SHELL of the respective Operating System and executes the command 'cls'
    os.system('cls')

#========================================================
    
#Nothing
#Day08

#User writes function using eval() | Get key of highest value from dictionary
#Day09
    
#========================================================

#1 - USING EVAL() FOR USER FUNCTION INPUT
    
#Allows for user input to use functions and evaluates those functions
x = 1
input = "x + 1" #string
print(eval(input)) # >> 2    

#Be careful using in big projects however as without proper restriction, it can be used to access os commands
#https://www.programiz.com/python-programming/methods/built-in/eval [read for more info]

#========================================================

#2 - GET KEY OF HIGHEST VALUE FROM DICTIONARY 
dict = {'a' : 3, 'b' : 7, 'c' : 2}

key = max(dict, key=dict.get)
# stats = {1: 2}
# func = stats.get  # Not called
# funct(1) >> stats.get(1) hence below...
# print(func(1))  # Prints 2
#https://www.reddit.com/r/pythonhelp/comments/xn5b8n/why_is_this_working_getting_key_of_max_value_from/ 

#========================================================

#Title case strings | Return multiple values
#Day10

#========================================================

#1 -  CONVERT STRING TO TITLE CASE

name = input("Enter name: ")
print(name.title())

#========================================================

#2 - RETURN MULTIPLE VALUES

def func():
    x=3; y="Dex"
    return x, y #returns tuple of x, y (3, "Dex")
num, name = func() #num = 3, name = "Dex"

#========================================================

#Condition needing at least one value | Sum values in list | How many times element reappears in list | Change instance of element x in list
#Day11

#========================================================

#1 - CONDITION NEEDING AT LEAST 1 VALUE

answer = input("Type 'a' or 'b' or 'c'.").lower()
if answer in ('a','b','c'):  #as long as answer is in the tuple (a,b,c)
    print("thanks")
else:
    print(":(")

if any([answer=='a', answer=='b', answer=='c']):
    print("this also works and can check multiple variables against multiple answers")

#========================================================

#2 - SUM VALUES IN LIST
list = [2, 4, 5]
sum(list) # 2+4+5 = 11

#========================================================

#3 - HOW MANY TIMES DOES ELEMENT REAPPEAR IN LIST
list = ['A', 'A', '4', 'J', 'A']
list.count('A') #3

#========================================================

#4 - CHANGE INSTANCE OF ELEMENT_X IN LIST
cards = ['A', 'A', '4', 'J', 'A']
cards[cards.index('A')] = 'K' #cards = ['K', 'A', '4', 'J', 'A'] run it again for ['K', 'K', '4', 'J', 'A']

#To change all instances
cards = list(map(lambda x: x.replace('A', 'K'), cards)) #cards = ['K', 'K', '4', 'J', 'K']


#Create text ASCII art
#Day12

#========================================================

#1 - CREATE TEXT ASCII ART

#lets you type in message and can copy the art for use.
#https://www.asciiart.eu/text-to-ascii-art 
    
#========================================================

#Nothing
#Day13

#Correctly using import
#Day14

#========================================================

#1 - CORRECTLY USING IMPORTS

#According to most data, it's best to place all imports at top of files for an easy glance.
#Imports can usually be sorted into 3 categories (Standard Library, Third Party, Local Application Modules)

#Standard library imports
import os 
import time

#Third party imports
import flask
import numpy

#Local application imports
import game_art

#Another note is to generally not use [from _library_ import *], this can lead to reduced readability and cluttered namespace.

#========================================================

#Rushed
#Day15

#Function Aliasing | Args and Kwargs | Assert keyword debugging | Loop with counter using enumerate
#Day16

#========================================================

#1 - FUNCTION ALIASING AND DECORATORS (@)

def f1(func):
    def wrapper():
        print("Started")
        func()
        print("Finished")
    #return function wrapper as an object
    return wrapper

#@f1 #IM A DECORATOR **************** toggle me on/off ********************
def random_function():
    print("Do a thingo here")

var_x = f1(random_function) #store function object in var_x
print(var_x) #prints: <function f1.<locals>.wrapper at 0x00E4DF34>

#var_x = f1(random_function)() | This will execute the function object (wrapper) with 0 arguments [Started\nDo a thingo here\nFinished]
#var_x() == f1(random_function)()

random_function()

#========================================================

#2 - UNKNOWN AMOUNT OF ARGUMENTS (ARGS AND KWARGS)

def printer(*args, **kwargs):
    print(args) #a tuple of args provided
    print("----")
    print(*args) #* is an -unpacking operator-
    print("----")
    print(kwargs)#a dict of keys and values
    print("----")
    for key, value in kwargs.items():
        print(f"{key} == {value}")
    print("*****************")

printer('a', 'b', 'c')
printer('yes', 'no')
printer('a', 'b', 'c', d=1, e=2, f=3)

#========================================================

#3 - DEBUGGING WITH ASSERT KEYWORD

x = 'Hi Dex'
assert x == 'Hi Dex' #nothing will happen
#assert x == 'Hi Jake' #raises a plain AssertionError, (like throwing an exception and breaking code)
assert x == 'Hi Jake', "x should be 'Hi Dex'"

#========================================================

#4 - LOOP WITH COUNTER USING ENUMERATE

iterable = ['a','b','c','d']
for idx, item in enumerate(iterable):
    pass

#...
#Day17

#========================================================

#1 - 