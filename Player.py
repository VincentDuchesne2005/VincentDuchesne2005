import Card
import random

class Player:

    #Take in one half of the game deck to initialize the player's deck
    def __init__(self, number):
        self.player_deck = []
        self.player_number = number

    def player_deck_shuffle(self):
        random.shuffle(self.player_deck)

    def get_number(self):
        return self.player_number

    def print_deck(self):
        deck = ''
        for cards in self.player_deck:
            deck += str(cards.get_value()) + " "
        print(deck)