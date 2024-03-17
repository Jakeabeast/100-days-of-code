import card_art
import random
from enum import Enum

class BlackJack():
    value_art = {'2' : (2, card_art.two), '3' : (3, card_art.three), '4' : (4, card_art.four),  '5': (5, card_art.five),
                 '6' : (6, card_art.six), '7' : (7, card_art.seven), '8' : (8, card_art.eight), '9': (9, card_art.nine),
                 '10': (10,card_art.ten), 'J' : (10,card_art.jack),  'Q' : (10,card_art.queen), 'K': (10,card_art.king),
                 'A' : (11,card_art.ace) }

    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', ]

    class GameStates(Enum):
        STARTING = 1
        PLAYING = 2
        STOP_DRAWING = 3

    STATES = ()
    def __init__(self):
        self.state = self.GameStates.STARTING
        self.player_cards = [] #fills with cards      ['4', 'Q', 'A']
        self.player_hand_value = [] #fills with values [4,  10,  11]
        self.dealer_cards = []
        self.dealer_hand_value = []

        self.game_over = False
        self.new_card = None

        for _ in range(2):
            start_card = random.choice(self.deck)
            self.player_cards.append(start_card)
            self.player_hand_value.append((self.value_art[start_card])[0])

        start_card = random.choice(self.deck)
        self.dealer_cards.append(start_card)
        self.dealer_hand_value.append((self.value_art[start_card])[0])

        print(card_art.logo)
        self.__rules()
        self.render()



    def __rules(self):
        HR = '-' * 120
        print(HR)
        print("Draw cards to score high. Don't go over 21 or you lose. Jack, Queen and King are worth 10 while Ace is worth 11 or 1.\n" + \
              "Keep drawing cards until you want to stop. If you are 21 or less, then the dealer draws cards.\n" + \
              "- You win by scoring higher than the dealer or if the dealer scores over 21\n" + \
              "- You lose by scoring over 21 or scoring less than the dealer\n" + \
              "- Scoring the same as the dealer results in a tie.")
        print(HR)

    def __valid_input(self):
        if self.new_card in ('y', 'n'):
            return True
        else:
            print(f"'{self.new_card}' is not a valid response.")
            return False


    def input(self):
        from os import system
        self.new_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        system('cls')

    def update(self):
        if not self.__valid_input():
            print("Try again.")
        else:
            if self.new_card == 'y':
                drawn_card = random.choice(self.deck)
                self.player_cards.append(drawn_card)
                self.player_hand_value.append((self.value_art[drawn_card])[0]) #*** may be error here
            else:
                self.state = self.GameStates.STOP_DRAWING
                return
            
        score = sum(self.player_hand_value)
        if score > 21:
            if 'A' in self.player_cards:
                self.player_hand_value[self.player_hand_value.index(11)] = 1
            else:
                self.game_over = True

    def render(self):
        if self.state == self.GameStates.STARTING:
            for card in self.player_cards:
                print(self.value_art[card][1])
            print(f"    Your starting hand: {self.player_cards}")
            print(f"    Dealers first card: {self.dealer_cards}")
            self.state = self.GameStates.PLAYING

        elif self.state == self.GameStates.PLAYING:
            for card in self.player_cards:
                print(self.value_art[card][1])
            print(f"    Your current hand is: {self.player_cards}")

        else:
            for card in self.player_cards:
                print(self.value_art[card][1])
            print(f"    Your final hand is: {self.player_cards}")





if __name__ == "__main__":
    game = BlackJack()
    while not game.game_over:
        game.input()
        game.update()
        game.render()
