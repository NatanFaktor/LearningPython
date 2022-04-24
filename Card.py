class Card:

    value_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    suit_list = ["Diamonds", "Spades", "Hearts", "Clubs"]


    def __init__(self, value, suit):
        if value in self.value_list:
            if value == 14:
                value = "Ace"
            if value == 13:
                value = "King"
            if value == 12:
                value = "Queen"
            if value == 11:
                value = "Jack"
            self.value = value
        if suit in self.suit_list:
            self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"

    def __gt__(self, other):
        if self.suit != other.suit:
            return self.suit_list.index(self.suit) > other.suit_list.index(other.suit)
        else:
            return self.value > other.value
    # def __gt__(self, other):
    #     if

if __name__ == "__main__":
    card1 = Card(11, "Diamonds")
    print(card1)
    # print("Clubs index", card1.suit_list.index("Clubs"))
    # print("Spades index", card1.suit_list.index("Spades"))

    card2 = Card(9, "Spades")
    print(card2)
    print(card1 > card2)
