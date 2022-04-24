from Card import Card
from random import *


class DeckOfCards:

    def __init__(self):
        self.deck = [Card(v, s) for v in Card.value_list for s in Card.suit_list]
        # self.deck = []
        # for v in range(2, 14):
        #     for s in Card.suit_list:
        #         self.deck.append(Card(v, s))

    def __str__(self):
        return f'my deck {self.deck}'

    def cards_shuffle(self):
        shuffle(self.deck)

    def deal_one(self):
        a = choice(self.deck)
        self.deck.remove(a)
        return a


if __name__ == "__main__":
    my_deck = DeckOfCards()
    print(my_deck)
    DeckOfCards.cards_shuffle(my_deck)
    print("Shuffle", my_deck)

    print(DeckOfCards.deal_one(my_deck))
    print(my_deck)
    print(my_deck)



