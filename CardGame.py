from Player import *

class CardGame:
    def __init__(self,player:Player,player2:Player):
        self.player=Player
        self.player2=Player
        self.plcards=player.num_cards
        self.pl2cards=player2.num_cards
        self.new_game()

    def new_game(self):
        mydeck=DeckOfCards()
        mydeck.cards_shuffle()
        self.player.set_hand(self.plcards)
        self.player2.set_hand(self.pl2cards)

    def get_winner(self):
        if len(self.player.set_hand(self.plcards))>len(self.player2.set_hand(self.pl2cards)):
            print(f'{self.player} is the winner')
        else:
            print(f'{self.player2} is the winner')
        if len(self.player.set_hand(self.plcards))==len(self.player2.set_hand(self.pl2cards)):
            return None
