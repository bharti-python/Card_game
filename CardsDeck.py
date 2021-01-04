#!/usr/bin/env python3
from Card import Card, Suite, Rank
from collections import deque
import random



class CardsDeck:
    '''
    CardsDeck class represents a deck of 52 cards (as per general standard) 
    for a card game.
    '''
    def __init__(self):
        '''
        A CardsDeck is created with all the 52 cards stored in sorted manner.
        '''
        self._cards = deque()
        self.refillDeck()

    def __str__(self):
        return ",".join([card.__str__() for card in self._cards])

    def sort(self):
        '''
        sorts the cards using python's sort method

        '''
        cardList = list(self._cards)
        cardList.sort(key=lambda card: (card.suite.value * len(list(Rank)) + card.rank.value))
        self._cards.clear()
        self._cards.extend(cardList)

    def shuffle(self):
        '''
        Refills the cards deck and then shuffles the cards 
        using python's random package shuffle method
        '''
        self.refillDeck()
        random.shuffle(self._cards)

    def getTopCard(self):
        '''
        As per problem statement, value of a card is defined as the 
        multiple of their suite and rank values.
        '''
        if len(self._cards) == 0:
            raise IndexError("Error: Deck is empty.")
        return self._cards.popleft()

    def refillDeck(self):
        '''
        As per problem statement, value of a card is defined as the 
        multiple of their suite and rank values.
        '''
        self._cards.clear()
        for suite in list(Suite):
            for rank in list(Rank):
                self._cards.append(Card(suite, rank))


if __name__ == "__main__":
    cardsDeck = CardsDeck()
    print(cardsDeck)
    cardsDeck.shuffle()
    print(cardsDeck)
    cardsDeck.sort()
    print(cardsDeck)
    print(cardsDeck.getTopCard())
    print(cardsDeck.getTopCard())
    print(cardsDeck)
    cardsDeck.refillDeck()
    print(cardsDeck)
    for i in range(len(list(Suite)) * len(list(Rank))):
        cardsDeck.getTopCard()
    try:
        cardsDeck.getTopCard()
    except IndexError as e:
        print(str(e))

    cardsDeck.shuffle()
    print(cardsDeck)
    print(cardsDeck.getTopCard())
    cardsDeck.shuffle()
    print(cardsDeck)
