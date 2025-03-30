class Card:

    #Take in a value from 1-13 and a suite
    def __init__(self, v, s):
        self.value = v
        self.suite = s

    def get_value(self):
        return self.value

    def get_suite(self):
        return self.suite

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

from Deck import Deck
from Player import Player

class WarGame:

    def __init__(self, num_player=2):
        self.game_deck = Deck()
        self.players = [Player(f"Player {i + 1}") for i in range(num_player)]
        self.deal_cards()
        
    #Separate the cards in two 26 cards deck for the players
    def deal_cards(self):
        mid = len(self.game_deck.deck) // 2
        self.players[0].player_deck = self.game_deck.deck[:mid]
        self.players[1].player_deck = self.game_deck.deck[mid:]

        for player in self.players:
            player.player_deck_shuffle()

    #Starts the game
    def start_game(self):
        print("Game started")

        for player in self.players:
            print(player.get_number())
            player.print_deck()

    #Continuously checks if a player has won 
        while self.check_win():
            self.play_round()

        print("Game ended")

    def play_round(self):
        card1 = self.players[0].player_deck.pop(0)
        card2 = self.players[1].player_deck.pop(0)
        discarded_cards = [card1, card2]

        if card1.get_value() > card2.get_value():
            self.players[1].player_deck.append(card2)
            self.players[1].player_deck.append(card1)
            print("Player 1 won the turn")
        elif card1.get_value() < card2.get_value():
            self.players[0].player_deck.append(card1)
            self.players[0].player_deck.append(card2)
            print("Player 2 won the turn")
        else:
            print("A battle has begun!")
            self.battle_ongoing(discarded_cards)

        for player in self.players:
                player.print_deck()

    def battle_ongoing(self, dis_cards):
        if len(self.players[0].player_deck) < 4 or len(self.players[1].player_deck) < 4:
            print("Not enough cards to battle!")
            self.players[0].player_deck.append(dis_cards[0])
            self.players[1].player_deck.append(dis_cards[1])

        else:
            cards_discarded = dis_cards
            for player in self.players:
                for i in range(3):
                    cards_discarded.append(player.player_deck[0])
                    player.player_deck.pop(0)

            card1 = self.players[0].player_deck.pop(0)
            card2 = self.players[1].player_deck.pop(0)

            if card1.get_value() > card2.get_value():
                self.players[1].player_deck.append(card1)
                self.players[1].player_deck.append(card2)
                for cards in cards_discarded:
                    self.players[1].player_deck.append(cards)
                print("Player 1 won the turn")
            elif card1.get_value() < card2.get_value():
                self.players[0].player_deck.append(card1)
                self.players[0].player_deck.append(card2)
                for cards in cards_discarded:
                    self.players[0].player_deck.append(cards)
                print("Player 2 won the turn")
            else:
                print("A battle has begun!")
                self.battle_ongoing(cards_discarded)

    def check_win(self):
        for player in self.players:
            if len(player.player_deck) == 0:
                print(f"{player.get_number()} has won! The other player looses")
                return False
        return True


# Run the game
game2 = WarGame()
game2.start_game()
  
