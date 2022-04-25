class Card:
    value_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]
    suit_list = ["Diamonds", "Spades", "Hearts", "Clubs"]

    def __init__(self, value, suit):
        if value in self.value_list:
            self.value = value
        if suit in self.suit_list:
            self.suit = suit

    def __repr__(self):
        if self.value == 1:
            return f"{'Ace'} of {self.suit}"
        elif self.value == 13:
            return f"{'King'} of {self.suit}"
        elif self.value == 12:
            return f"{'Queen'} of {self.suit}"
        elif self.value == 11:
            return f"{'Jack'} of {self.suit}"
        else:
            return f"{self.value} of {self.suit}"

    def __gt__(self, other):
        """Gets two cards and returns True if the first one is grater then the other"""
        if self.value != other.value:
            return self.value_list.index(self.value) > other.value_list.index(other.value)
        else:
            return self.suit_list.index(self.suit) > other.suit_list.index(other.suit)


if __name__ == "__main__":
    card1 = Card(1, "Diamonds")
    print(card1)
    # print("Clubs index", card1.suit_list.index("Clubs"))
    # print("Spades index", card1.suit_list.index("Spades"))

    card2 = Card(9, "Spades")
    print(card2)
    print(card1 > card2)
