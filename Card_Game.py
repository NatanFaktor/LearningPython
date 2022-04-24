from Player import *


class CardGame:
    def __init__(self, player: Player, player2: Player):
        self.player = player
        self.player2 = player2
        self.pcards = player.num_cards
        self.p2cards = player2.num_cards
        self.new_game()

    def new_game(self):
        mydeck = DeckOfCards()
        mydeck.cards_shuffle()
        self.player.set_hand()
        self.player2.set_hand()

    def get_winner(self):
        if len(self.player.playerdeck) == len(self.player2.playerdeck):
            print("It's a tie")
        elif len(self.player.playerdeck) > len(self.player2.playerdeck):
            print(f'{self.player.playername} is the winner')
        else:
            print(f'{self.player2.playername} is the winner')


if __name__ == "__main__":
    p1 = Player("Natan")
    p2 = Player("Gavriel")
    war = CardGame(p1, p2)
    print(p1)
    print(p1.playerdeck)
    print(p2)
    print(p2.playerdeck)
