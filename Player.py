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

    def set_hand(self):
        for i in range(self.num_cards + 1):
            a = self.mydeck.deal_one()
            self.playerdeck.append(a)
        return self.playerdeck

    def get_card(self):
        randchoice = choice(self.playerdeck)
        self.playerdeck.remove(randchoice)
        return randchoice

    def add_card(self, card: Card):
        for i in self.playerdeck:
            if i == card:
                self.playerdeck.remove(i)
                self.playerdeck.append(card)

                break
        # if card not in self.playerdeck:
        #     self.playerdeck.append(card)
        # return



if __name__ == "__main__":
    p1 = Player("Natan", 20)
    p1.set_hand()
    print(p1.playerdeck)
    print(p1.get_card())
    print(p1.playerdeck)
    p1.add_card(Card(11, "Diamonds"))
    print(p1.playerdeck)
