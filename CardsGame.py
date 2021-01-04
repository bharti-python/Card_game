#!/usr/bin/env python3
'''
This is a card deck game program.
How to play:
    Two players are required for this game.
    Players play turn by turn as per instructions on the screen.
'''

from __future__ import print_function
from CardsDeck import CardsDeck
from Card import Card
import os

class CardsGame:
    def __init__(self):
        self._cardsDeck = CardsDeck()

    def printMainScreen(self):
        mainScreenMessage = """
        Cards game options:
        1. Refill and shuffle card deck
        2. Get a card from Top of the deck
        3. Sort cards (Won't refill deck)
        4. Play the '3 card max score' game
        5. Print current deck of cards
        6. Exit the cards game
        """

        print(mainScreenMessage)

    CHOICE_SHUFFLE = 1
    CHOICE_TOP_CARD = 2
    CHOICE_SORT = 3
    CHOICE_PLAY = 4
    CHOICE_PRINT = 5
    CHOICE_EXIT = 6

    def clearScreen(self):
        if os.name is 'posix':
            os.system('clear')
        else:
            os.system('cls')

    def playWithCards(self):
        self.clearScreen()
        print("Welcome to playing cards game!")
        gameOn = True
        while gameOn:
            try:
                self.printMainScreen()
                option = int(input("Please choose an option: "))
            except ValueError:
                print("Error: Invalid option, please choose from the given options!\n")
                continue
            gameOn = self.executeGameOption(option)

    def executeGameOption(self, option: int) -> bool:
        if option < self.CHOICE_SHUFFLE or option > self.CHOICE_EXIT:
            print("Error: Invalid option, please choose from the given options!\n")
            return True
        elif option == self.CHOICE_SHUFFLE:
            self._cardsDeck.shuffle()
            print(f"Cards have been shuffled, if you want to see the cards in the card deck," 
            f"please choose option {self.CHOICE_PRINT} on main screen\n")
            return True
        elif option == self.CHOICE_TOP_CARD:
            card = self._cardsDeck.getTopCard()
            print(f"The card received from top is: {card}\n")
            return True
        elif option == self.CHOICE_SORT:
            self._cardsDeck.sort()
            print(f"Cards have been sorted, if you want to see the cards in the card deck," 
            f"please choose option {self.CHOICE_PRINT} on main screen\n")
            return True
        elif option == self.CHOICE_PLAY:
            self.playMaxScoreGame()
            input()
            return True
        elif option == self.CHOICE_PRINT:
            print(f"Current set of playing cards are:\n {self._cardsDeck}\n")
            return True
        else: #option == self.CHOICE_EXIT
            print("Thanks for playing cards game, See you again soon!")
            return False

    def playMaxScoreGame(self):       
        MAX_PLAY_TURNS = 3
        PLAYERS_COUNT = 2
        playersScores = [0] * (PLAYERS_COUNT+1)

        for turn in range(1, MAX_PLAY_TURNS+1):
            for playerNumber in range(1, PLAYERS_COUNT+1):
                playersScores[playerNumber] += self.playTurn(playerNumber)
                print(f"Player {playerNumber} total score after {turn} round(s): {playersScores[playerNumber]}\n")

        maxScore = max(playersScores)
        maxScorePlayer = playersScores.index(maxScore)
        print(f"Player {maxScorePlayer} Wins with score = {maxScore}!")

    def playTurn(self, playerNumber: int):
        input(f"Player {playerNumber}, please press enter to receive a card:")
        card = self._cardsDeck.getTopCard()
        print(f"Player {playerNumber} received card: {card}, which has score={card.getValue()}")
        return card.getValue()
