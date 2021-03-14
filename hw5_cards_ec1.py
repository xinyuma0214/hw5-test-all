import random
import unittest

VERSION = 0.01
 
class Card:
    '''a standard playing card
    cards will have a suit and a rank
    Class Attributes
    ----------------
    suit_names: list
        the four suit names in order 
        0:Diamonds, 1:Clubs, 2: Hearts, 3: Spades
    
    faces: dict
        maps face cards' rank name
        1:Ace, 11:Jack, 12:Queen,  13:King
    Instance Attributes
    -------------------
    suit: int
        the numerical index into the suit_names list
    suit_name: string
        the name of the card's suit
    rank: int
        the numerical rank of the card
    rank_name: string
        the name of the card's rank (e.g., "King" or "3")
    '''
    suit_names = ["Diamonds","Clubs","Hearts","Spades"]
    faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}
 

    def __init__(self, suit=0,rank=2):
        self.suit = suit
        self.suit_name = Card.suit_names[self.suit]

        self.rank = rank
        if self.rank in Card.faces:
            self.rank_name = Card.faces[self.rank]
        else:
            self.rank_name = str(self.rank)
 
    def __str__(self):
        return f"{self.rank_name} of {self.suit_name}"
 

class Deck:
    '''a deck of Cards
    Instance Attributes
    -------------------
    cards: list
        the list of Cards currently in the Deck. Initialized to contain
        all 52 cards in a standard deck
    '''

    def __init__(self): 

        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card) # appends in a sorted order
 
    def deal_card(self, i=-1):
        '''remove a card from the Deck
        Parameters  
        -------------------
        i: int (optional)
            the index of the ard to remove. Default (-1) will remove the "top" card
        Returns
        -------
        Card
            the Card that was removed
        '''
        return self.cards.pop(i) 
 
    def shuffle(self):
        '''shuffles (randomizes the order) of the Cards
        self.cards is modified in place
        Parameters  
        ----------
        None
        Returns
        -------
        None
        '''
        random.shuffle(self.cards)
 
    def replace_card(self, card):
        card_strs = [] # forming an empty list
        for c in self.cards: # each card in self.cards (the initial list)
            card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
        if card.__str__() not in card_strs: # if the string representing this card is not in the list already
            self.cards.append(card) # append it to the list
    
    def sort_cards(self):
        '''returns the Deck to its original order
        
        Cards will be in the same order as when Deck was constructed.
        self.cards is modified in place.
        Parameters  
        ----------
        None
        Returns
        -------
        None
        '''
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card)
 
    def deal_hand(self, hand_size):
        '''removes and returns hand_size cards from the Deck
        
        self.cards is modified in place. Deck size will be reduced
        by hand_size
        Parameters  
        -------------------
        hand_size: int
            the number of cards to deal
        Returns
        -------
        list
            the top hand_size cards from the Deck
        '''
        hand_cards = []
        for i in range(hand_size):
            hand_cards.append(self.deal_card())
        return hand_cards

def print_hand(hand):
    '''prints a hand in a compact form
    
    Parameters  
    -------------------
    hand: list
        list of Cards to print
    Returns
    -------
    none
    '''
    hand_str = '/ '
    for c in hand:
        s = c.suit_name[0]
        r = c.rank_name[0]
        hand_str += r + "of" + s + ' / '
    print(hand_str)

class Hand:
    '''a hand for playing card
    Instance Attributes
    -------------------
    init_card: list
        a list of card
    '''
    def __init__(self,init_cards):
        self.init_card = init_cards
        
    def add_card(self,card):
        '''add a card

        parameter
        -------------------
        card: instance
            a card to add

        returns
        -------------------
        None
        '''
        if card not in self.init_card:
            self.init_card.append(card)

    def remove_card(self,card):
        '''remove a card from the hand

        for testing, I create object of Hand, assign the init_card to [1,2,3,4,5],
        when remove card 3, the return will be 3. And I test the init_card list to 
        approve that function.

        parameter
        -------------------
        card: instance
            a card to remove

        returns
        -------------------
        the card, or None if the card was not in the hand
        '''
        i = 0
        if card in self.init_card:
            for c in self.init_card:
                if card == c:
                    return self.init_card.pop(i) 
                i += 1
        
    def draw(self,deck):
        '''draw a card

        For testing this function, I create a object of Deck named deck 
        and a object of Hand([1,2,3,4,5]) named eq3.
        
        the len(deck.cards) is 52 at the beginning, and after call the function draw(deck),
        len(deck.cards) will be 51.

        the len(eq3.init_card) is 5 at the beginning, and after call the function draw(deck),
        len(eq3.init_card) will be 6.
        parameter
        -------------------
        deck: instance
            a deck from which to draw

        returns
        -------------------
        None
        '''
        card = deck.deal_card()
        self.add_card(card)
    