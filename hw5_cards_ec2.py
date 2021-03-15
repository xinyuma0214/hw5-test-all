import random
import unittest
import numpy as np

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

    def deal(self, num_of_hands, num_of_cards_per_hand):
        '''removes cards in the deck and add them to the hand
        
        self.cards,hand_cards will be modified. Deck size will be reduced
        and hand_cards will be increased.
        After shuffling the cards, this function will deal the number of cards
        equals to num_of_cards_per_hand to the first hand, then the second, third,
        ... ,last hand in turn.

        for testing this function, I use eq2 = hw5_cards_ec2.Deck() to
        create a object for Deck. Parameter use (3,-1) 
        to test all of the card being dealt to three hands, the number of each hand
        will be 18,17,17.

        Parameters  
        -------------------
        num_of_hands: int
            the number of hands
        num_of_cards_per_hand: int
            the number of cards per hand
        Returns
        -------
        list
            a list of hands
        '''
        res_list = []
        self.shuffle()
        if num_of_cards_per_hand == -1:
            even_num = 52 // num_of_hands
            for i in range(num_of_hands):
                res_list.append(self.deal_hand(even_num))
            remaining_num = 52 - (even_num * num_of_hands)
            for i in range(remaining_num):
                res_list[i].append(self.deal_hand(1)[0])
        else:
            # hand_list = [[] for _ in range(n)]
            for i in range(num_of_hands):
                res_list.append(self.deal_hand(num_of_cards_per_hand)) 
        
        return res_list   





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
    def __init__(self, init_cards):
        self.init_cards = init_cards
        
    def add_card(self,card):
        if card not in self.init_cards:
            self.init_cards.append(card)

    def remove_card(self,card):
        i = 0
        if card in self.init_cards:
            for c in self.init_cards:
                if card == c:
                    return self.init_cards.pop(i) 
                i += 1
        
    def draw(self,deck):
        card = deck.deal_card()
        self.init_cards.add_card(card)
    
    def remove_pairs(self):
        '''
        remove the pairs that are two same numbers in the hand

        First, Find duplicate card in the hand and append it to the list:list_of_duplicate, 
        then use set() to remove duplicate in that list.
        Second, iterate through that list to find the index of every duplicate cards,
        fetch first two indices of each card's duplicate location and append those two indices into
        list:index_of_dup.
        Third, iterate thorugh the list of index and pop those card. 

        For testing the function, I create a object of Hand with list [1,1,1,2,2,3,4,5].
        after call this function, the init_card list will be [1,3,4,5]


        Parameters
        ----------       
        self 
        
        Returns
        -------
        the card list in the hand after the pair of the cards being removed
        '''
        l1 = []
        list_of_duplicate = []
        index_of_dup = []
        for c in self.init_cards:
            if c not in l1:
                l1.append(c)
            else:
                list_of_duplicate.append(c)
        list_of_duplicate = list(set(list_of_duplicate))
        for c in list_of_duplicate:
            indices = [index for index, value in enumerate(self.init_cards) if value == c]
            # print(indices)
            num = 0
            for i in indices:
                if num <= 1:
                    index_of_dup.append(i)
                num += 1
        # print(index_of_dup) -->[0,1,2,3]
        for i in sorted(index_of_dup, reverse=True):          
            self.init_cards.pop(i) 
            # print(self.init_cards[i])
        return self.init_cards
    



    # def get_index1(self,lst=None, item=''):
    #     return [index for (index,value) in enumerate(lst) if value == item]
