from game_cards.Card import Card

""""""
class DeckOfCards:

    def __init__(self):
        self.deck_list=[]
        for i in range(1,5):
            for j in range(1,14):
                self.deck_list.append(Card(j,i))

    
    def __repr__(self):
        return f"Deck of Cards {self.deck_list}"

deck=DeckOfCards()
print(deck.deck_list)