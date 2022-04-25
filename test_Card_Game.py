from unittest import TestCase
from Player import Player
from Card_Game import CardGame


class TestCardGame(TestCase):

    def test__init__valid(self):
        self.new_game = CardGame("Natan", 20, "Gavriel", 21)
        self.assertEqual(self.new_game.player.playername, "Natan")
        self.assertEqual(self.new_game.player2.playername, "Gavriel")
        self.assertEqual(len(self.new_game.player.playerdeck), 20)
        self.assertEqual(len(self.new_game.player2.playerdeck), 21)

        self.new_game = CardGame("Amit", 27, "Natan", 150)
        self.assertEqual(len(self.new_game.player.playerdeck), 26)
        self.assertEqual(len(self.new_game.player2.playerdeck), 26)

        self.new_game = CardGame("Amit", 9, "Natan", 10)
        self.assertEqual(len(self.new_game.player.playerdeck), 26)
        self.assertEqual(len(self.new_game.player2.playerdeck), 10)

    def test__init__invalid(self):
        with self.assertRaises(TypeError):
            self.new_game = CardGame(123, 15, "Gavriel", 15)
        with self.assertRaises(TypeError):
            self.new_game = CardGame("Natan", "Amit", "Gavriel", 15)
        with self.assertRaises(TypeError):
            self.new_game = CardGame("Natan", 15, 69, 15)
        with self.assertRaises(TypeError):
            self.new_game = CardGame("Natan", 15, "Gavriel", 1.54)

    def test_new_game(self):
        self.new_game = CardGame("Natan", 20, "Gavriel", 21)
        for i in self.new_game.player.playerdeck:
            self.assertNotIn(i, self.new_game.player2.playerdeck)

    def test_get_winner(self):
        self.new_game = CardGame("Natan", 20, "Gavriel", 20)
        self.assertEqual(CardGame.get_winner(self.new_game), None)
        self.new_game = CardGame("Natan", 20, "Gavriel", 21)
        self.assertEqual(CardGame.get_winner(self.new_game), False)
        self.new_game = CardGame("Natan", 21, "Gavriel", 20)
        self.assertEqual(CardGame.get_winner(self.new_game), True)






