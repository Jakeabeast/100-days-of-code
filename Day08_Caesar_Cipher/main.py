'''
DAY 8 PROJECT - Ceasar Cipher

The goal of this project is to recreate the ceasar cipher, capable of crypting and decrypting messages using Ceasers algorithm. 
In contrast to the previous project, I wanted to take a procedural apporach and compare it to the OOP approach.
Specifically I'm looking to compare the pros and cons of each style of coding and what I prefer and why.
'''

from art import logo

alphabet = list(map(chr, range(97, 123))) #['a', 'b'... 'z']
def welcome():
    print(logo)

def encrypt(message, shift_value):
    str = ""
    for char in message:
        if char != ' ':
            shifted_ascii_value = ((ord(char) - 96 + shift_value) % 26) + 96
            if shifted_ascii_value == 96: shifted_ascii_value = 122
            str += chr(shifted_ascii_value)
        else:
            str += ' '
    return str

def decrypt(crypt_message, shift_value):
    str = ""
    for char in crypt_message:
        if char != ' ':
            shifted_ascii_value = ((ord(char) - 96 - shift_value) % 26) + 96
            if shifted_ascii_value == 96: shifted_ascii_value = 122
            str += chr(shifted_ascii_value)
        else:
            str += ' '
    return str

if __name__ == '__main__':
    welcome()
    loop = True
    while loop:
        print("Type \"encode\" to encrypt, type \"decode\" to decrypt.")
        choice = input().lower()
        if choice == "encode":
            msg = input("\nType your message >> ")
            num = input("Type the shift value >> ")
            print("\nHere's the encoded result: " + encrypt(msg, int(num)))
        elif choice == "decode":
            code = input("\nType your encrpyted message >> ")
            num = input("Type the shift value >> ")
            print("\nHere's the decoded result: " + decrypt(code, int(num)))
        else:
            print("Please only type \"encode\" or \"decode\".")
            continue

        print("Type \"yes\" if you want to go again. Otherwise type \"no\".")
        choice = input().lower()
        loop = False if choice == "no" else True
    
    print("Goodbye!")
  
#P.S I prefer OOP, though it does take longer to setup which isnt worth for small sized projects