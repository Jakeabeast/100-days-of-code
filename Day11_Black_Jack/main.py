import card_art

class BlackJack():
    value_art = {'2' : (2, card_art.two), '3' : (3, card_art.three), '4' : (4, card_art.four),  '5': (5, card_art.five),
                 '6' : (6, card_art.six), '7' : (7, card_art.seven), '8' : (8, card_art.eight), '9': (9, card_art.nine),
                 '10': (10,card_art.ten), 'J' : (10,card_art.jack),  'Q' : (10,card_art.queen), 'K': (10,card_art.king),
                 'A' : (11,card_art.ace) }

    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', ]

    def __init__(self):
        self.player_cards = []
        self.player_hand_value = 0
        self.dealer_cards = []
        self.dealer_hand_value = 0

        self.new_card = None

        print(card_art.logo)
        self.__rules()

    def __rules(self):
        pass

    def input(self):
        pass

    def update(self):
        pass

    def render(self):
        pass


if __name__ == "__main__":
    game = BlackJack()
