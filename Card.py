#!/usr/bin/env python3
from enum import Enum


class Suite(Enum):
    '''
    Suite class represents a specific suite in playing cards
    Generally the enumerations are all UPPER case, but here I
    am using the general writing style case so that its helpful for
    displaying. Otherwise I could also implement __str__ and __repr__ methods
    to display names in different format.
    '''

    '''Implementation assumptions:
    Here we have used Enum as the base class to maintain the fixed set of
    range and values possible for a Suite.
    I could implement this Suite class also in same manner as Rank but I have
    kept it here as Enum to show the usage of Enum although it is slightly 
    inconsistent to use two different ways to implement two such classes.
    '''
    Spades = 1
    Diamonds = 2
    Hearts = 3
    Clubs = 4


class IterableRank(type):
    def __iter__(cls):
        return iter(cls._nameToValueMap)


class Rank(metaclass=IterableRank):
    '''
    Rank class represents rank of a card.
    Here, although not defined in  the problem, we are using Ace's value
    as 14 since problem states that Ace should be the high value.
    '''

    '''Implementation assumptions:
    Here we can't use Enum as base class since we want to use numeric literals 
    as values.I could also use Enum with values like "one" instead of "1".
    For now, I assume that using values like "1" are necessary, otherwise 
    this class could be much simpler same as above Suite class.

    For now, this class becomes like a pseudo-enum class where the only 
    difference is that constructor requires string based names instead 
    of Enum values.
    '''

    _nameToValueMap = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "Jack": 11,
        "Queen": 12,
        "King": 13,
        "Ace": 14,
    }

    def __init__(self, name: str):
        if name not in Rank._nameToValueMap:
            raise TypeError(f"{name} is not a card Rank, "
                "please use correct Rank value.")
        
        self._name = name

    def __getattribute__(self, attribute):
        if attribute == "value":
            return Rank._nameToValueMap[self._name]
        if attribute == "name":
            return self._name
        if attribute in Rank._nameToValueMap:
            return attribute
        return super().__getattribute__(attribute)

    def __repr__(self):
        return f"Rank(rank={self.name})"

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def __iter__(cls):
        return cls._nameToValueMap


class Card:
    '''
    Card class represents a single card for a card game.
    '''
    def __init__(self, suite: Suite, rank):
        self.suite = suite
        self.rank = Rank(rank)

    def __repr__(self):
        return f"Card(suite={self.suite.name}, rank={self.rank.name})"

    def __str__(self):
        return f"({self.suite.name} {self.rank.name})"

    def __lt__(self, other):
        return self.getValue() < other.getValue()

    def __le__(self, other):
        return self.getValue() <= other.getValue()

    def __eq__(self, other):
        return self.getValue() == other.getValue()

    def getValue(self):
        '''
        As per problem statement, value of a card is defined as the 
        multiple of their suite and rank values.
        '''
        return (self.suite.value * self.rank.value)
