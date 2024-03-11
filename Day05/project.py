'''
DAY 5 PROJECT - Password Generator

The goal of this project is to recreate a random password generator that can be tailored with some input. 
I've decided to explore multiple methods of generating parts of the password.
'''

#=========================================================================

'''
----ASCII----
A - Z = [65 - 90]
a - z = [97 - 122]

----Numbers----
0 - 9 Use generic values

----Symbols List----
symbols created in list, grab from that list specific values
'''

import random

ASCII_A = 65; ASCII_Z = 90
ASCII_LOWER_A = 97; ASCII_LOWER_Z = 122

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

password = []
for _ in range(1, num_letters + 1):
    #select evenly between ascii upper or lowercase values 
    ascii_value = random.randint(ASCII_A, ASCII_Z) if random.randint(0,1) == 0 \
             else random.randint(ASCII_LOWER_A, ASCII_LOWER_Z)
    
    password.append(chr(ascii_value))

for _ in range(1, num_symbols + 1):
    password.append(random.choice(symbols))

for _ in range(1, num_numbers + 1):
    password.append(str(random.randint(0,9)))

random.shuffle(password)
print("Here is your password: " + ''.join(password))