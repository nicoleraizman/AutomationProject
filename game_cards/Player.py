from game_cards.DeckOfCards import DeckOfCards
from game_cards.Card import Card
import random
"""Import random in order to create a get_card function below"""

class Player:

    def __init__(self, name, number_of_cards=26):
        """Function that receives a name of a player and a number of cards
        which is 26 by default. The method also initializes the deck of cards as
        an empty list for every player and also makes sure the name of the players is of string class
        and the number of cards is of integer class by calling the appropriate functions (below)"""
        self.player_name = self.enter_string(name)
        self.player_deck = []
        if number_of_cards < 10 or number_of_cards > 26:
            self.player_cards = 26
        else:
            self.player_cards = self.enter_int(number_of_cards)

    def __repr__(self):
        """Function that returns a Player name and the player's deck of cards"""
        return f"Player {self.player_name}, your deck of cards is {self.player_deck}"

    def set_hand(self,deck:DeckOfCards):
        """Function that receives a deck of cards and gives random cards to every player
        according to the amount, which the players have to receive"""
        for i in range(self.player_cards):
            self.player_deck.append(deck.deal_one())

    def get_card(self):
        """Function that gets a random card from the player's deck and removes it from deck.
        The function returns the chosen card"""
        variant = random.choice(self.player_deck)
        self.player_deck.remove(variant)
        return variant

    def add_card(self,card:Card):
        """Function that receives a card and adds it to the deck of player"""
        self.player_deck.append(card)

    def enter_string(self,name):
        """An additional function that checks whether the name of the players is from the string class.
        If the name is not a string, the function will commit the procedure of exception handling"""
        while True:
            if type(name) == str:
                break
            else:
               try:
                    name = input("Enter the name again: ")
                    break
               except ValueError:
                    print("Invalid value, must be string. Enter again: ")

    def enter_int(self, number_of_cards):
        while True:
            if type(number_of_cards) == int:
                break
            else:
               try:
                    number_of_cards = input("Enter the Number of cards again: ")
                    break
               except ValueError:
                    print("Invalid value, must be integer. Enter again: ")