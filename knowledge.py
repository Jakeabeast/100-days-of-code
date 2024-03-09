'''
Just for clarification, this knowledge.py files will be used to store ideas and featrures that I explored.
The structure will be a day by day basis.
I will use folding to fold up each day with a summary of what there is within that section

'''

#Instant Variable Swap, Code Intelligence, Reuse specific function from imported library, Aliasing library
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

#Interpolation Operator (string formatting), line shift and duplication, manual fold, rounding float
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
round(num, 3) # = 2.667

num = 8//3 # = 2 (int)

#note that below is apparently a float (could easily be used as int though since python is so dynamic at casting data types)
num = 4 / 2

#===============================================================

#Tenary Operator (conditional statement with result), ASCCI art, Commenting shortcut
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

