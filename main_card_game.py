from Card import Card
from DeckOfCards import DeckOfCards
from Card_Game import CardGame
from Player import Player

p1 = Player("Natan", 26)
p2 = Player("Gavriel", 26)
new = CardGame(p1, p2)


print(p1.playerdeck)
print(len(p1.playerdeck))
print(p2.playerdeck)
print(len(p2.playerdeck))

for i in range(-8):
    a = p1.get_card()
    b = p2.get_card()
    print(f"{p1.playername} threw {a}")
    print(f"{p2.playername} threw {b}")
    if a > b:
        p1.add_card(b)
        p2.playerdeck.remove(b)
        print(f"{p1.playername} won this round\n")
    else:
        p2.add_card(a)
        p1.playerdeck.remove(a)
        print(f"{p2.playername} won this round\n")
new.get_winner()
print(len(p1.playerdeck))
print(p1.playerdeck)
print(len(p2.playerdeck))
print(p2.playerdeck)
# from Card_Game import *
#
# player1 = Player('natan', 26)
# print(player1)
# player2 = Player('gavriel', 26)
# print(player2)
# print('------------------Game Starting-----------------------')
# mygame = CardGame(player1, player2)
# rounds = 0
# while rounds != 10:
#     rounds += 1
#     a = player1.get_card()
#     b = player2.get_card()
#     if a > b:
#         player1.playerdeck.append(b)
#     else:
#         player2.playerdeck.append(a)
#     print(len(player1.playerdeck))
#     print(f'Player 1 Thrown Card : {player1.get_card()},Player 2 Thrown Card: {player2.get_card()}')
#
