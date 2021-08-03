import random 
from collections import deque

class CardDeck(object):
    def __init__(self, name, total):
        self.game_name = name
        self.all_cards = total
        self.deck = []
        self.used_cards = []
        self.current_total = 0
        
    def ordinary_cards(self, name, number, start=0, twice=False):
        if number > self.all_cards:
            return "Invalid number of cards!"
        if self.all_cards == 0:
            return "Maximum number of cards reached."
        
        cards_to_deck = []
        for i in range(start, number+1):
            if twice != False:
                for j in range(2):
                    cards_to_deck.append((name, i))
            else:
                cards_to_deck.append((name, i))
        self.all_cards -= len(cards_to_deck)
        self.deck += cards_to_deck
        self.current_total += len(cards_to_deck)
        
    def special_cards(self, name, number):
        if number > self.all_cards:
            return "Invalid number of cards!"
        if self.all_cards == 0:
            return "Maximum number of cards reached."
        
        self.all_cards -= number
        self.current_total += number
        for i in range(1, number+1):
            self.deck.append((name, i))
            
    def shuffle(self):
        return random.shuffle(self.deck)
    
    def draw_cards(self):
        self.used_cards.append(self.deck[-1])
        self.deck.pop()
        self.current_total = len(self.deck)
