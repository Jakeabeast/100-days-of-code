import random
import hangman_words
from hangman_art import logo, stages
from os import system

class Hangman():
    word_list = hangman_words.word_list

    def __init__(self):
        self.word_to_guess = random.choice(self.word_list)
        self.word_length = len(self.word_to_guess)
        self.revealed_word = ['_'] * self.word_length
        self.guesses_remaining = 7
        self.incorrect_guesses = []
        self.letter_guess = None
        self.winner = None

        self.__welcome()
        self.render()

    def __welcome(self):
        print(logo)
        print("Welcome to Hangman.\nGuess the hidden word to win.")

    def __end_screen(self):
        print('\n')
        print(list(self.word_to_guess))
        if self.winner == True:
            print("You survived with %i remaining guesses." % self.guesses_remaining)
            print("Goodbye!")
        else:
            HR = '-' * 20
            print("%s\nBad luck, you lose!\n%s" % (HR, HR))

    def input(self):
        self.letter_guess = input().lower()
        system('cls') #***

    def update(self):
        correct_guess = False
        win = True
        guess = self.letter_guess

        if len(guess) > 1:
            print("Can only guess a single character.\nTry again.")
            return
        elif len(guess) == 0:
            print("Please enter at least something.\nTry again.")
            return
        #go through every letter in hidden word
        for idx in range(0,self.word_length):
            if guess == self.word_to_guess[idx]:
                correct_guess = True
                #guess correct and not revealed yet
                if self.revealed_word[idx] == '_':
                    self.revealed_word[idx] = guess
                else:
                    print("You already guessed the letter %s." % guess)
                    win = False
                    break 
            elif self.revealed_word[idx] == '_':
                win = False
        
        #incorrect guess
        if correct_guess == False:
            self.guesses_remaining -= 1
            self.incorrect_guesses.append(guess)
            if self.guesses_remaining <= 0:
                self.winner = False
        elif win == True:
            self.winner = True           

    def render(self):
        if self.winner == None:
            print("Remaining Guesses: %s" % self.guesses_remaining)
            if self.incorrect_guesses != []:
                print("Incorrect guesses " + str(self.incorrect_guesses))
            print(stages[self.guesses_remaining-1])
            print(self.revealed_word)
            print("\nYour next letter >> ", end='')

        else: 
            self.__end_screen()

    

if __name__ == "__main__":
    game = Hangman()

    while game.winner == None:
        game.input()
        game.update()
        game.render()