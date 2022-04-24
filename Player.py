from DeckOfCards import *
from random import *


class Player:
    def __init__(self, playername: str, num_cards: int = 26):
        self.playername = playername
        self.num_cards = num_cards
        if self.num_cards < 10 or self.num_cards > 26:
            self.num_cards = 26
        self.playerdeck = []
        self.mydeck = DeckOfCards()

    def __str__(self):
        return f"{self.playername} with {len(self.playerdeck)} cards"

    def set_hand(self):
        while len(self.playerdeck) != self.num_cards:
            a = self.mydeck.deal_one()
            self.playerdeck.append(a)
        # return self.playerdeck

    def get_card(self):
        randchoice = choice(self.playerdeck)

        # self.playerdeck.remove(randchoice)
        return randchoice

    def add_card(self, card: Card):
        self.playerdeck.append(card)




if __name__ == "__main__":
    my_deck = DeckOfCards()
    print(my_deck)
    p1 = Player("Natan", 20)
    p2 = Player("Gavriel", 25)
    print(p1.playerdeck)
    print(p2.playerdeck)

    p1.set_hand()
    p2.set_hand()
    print("P1", p1.playerdeck)
    print("Get Card", p1.get_card())
    print(len(p1.playerdeck))
    print("P1", p1.playerdeck)
    print(len(p2.playerdeck))
    print("P2", p2.playerdeck)
    p1.add_card(Card(11, "Diamonds"))
    print("Add Card", p1.playerdeck)
    print(p1)
    print(p2)
