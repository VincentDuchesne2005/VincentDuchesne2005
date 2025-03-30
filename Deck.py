from Card import Card
import random

class Deck:

    #Initializes a normal deck of 52 cards
    def __init__(self):
        self.deck = []
        suite = {
            0: "Spade",
            1: "Heart",
            2: "Diamond",
            3: "Club",
        }
        for values in range(1, 14):
            for count in range(4):
                self.deck.append(Card(values, suite[count]))
        random.shuffle(self.deck)

    def print(self):
        for items in self.deck:
            print(f"{items.get_value()} {items.get_suite()}")


