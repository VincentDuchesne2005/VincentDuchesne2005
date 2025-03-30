from Deck import Deck
from Player import Player

class WarGame:

    def __init__(self, num_player=2):
        self.game_deck = Deck()
        self.players = [Player(f"Player {i + 1}") for i in range(num_player)]
        self.deal_cards()

    def deal_cards(self):
        mid = len(self.game_deck.deck) // 2
        self.players[0].player_deck = self.game_deck.deck[:mid]
        self.players[1].player_deck = self.game_deck.deck[mid:]

        for player in self.players:
            player.player_deck_shuffle()

    def start_game(self):
        print("Game started")

        for player in self.players:
            print(player.get_number())
            player.print_deck()

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