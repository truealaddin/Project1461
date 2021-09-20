from Deck import Deck
from Hand import Hand
from enum import Enum
from Card import Card

class Counts(Enum):
    Pass = 0
    Part = 1
    Game = 2
    Small_Slam = 3
    Grand_Slam = 4

class Simulator:
    def __init__(self, info):
        self.deck = Deck(info)
        self.original = info
        self.hand = Hand()
        self.cycle = 0
        self.counts = [0, 0, 0, 0, 0]
        self.outcome = [0,0,0,0,0]
        self.outcomeNames = ["Pass", "Part", "Small Slam", "Grand Slam"]

    def DealSelf(self):

        for _ in range(13):
            self.hand.AddCard(self.deck.DealCard())
        self.ResetDeck()
    def ResetDeck(self):
        self.deck.deck = self.original.copy()
    def ResetHand(self):
        self.hand = Hand()
    def RunSimulation(self, x_times, otherPoints):
        print("Running plays......\n")
        self.cycle = x_times
        for _ in range(x_times):
            self.DealSelf()
            self.hand.CalculatePoints(otherPoints)
            if self.hand.points < 20:
                self.counts[Counts.Pass.value] += 1
            elif self.hand.points <= 25:
                self.counts[Counts.Part.value] += 1
            elif self.hand.points <= 31:
                self.counts[Counts.Game.value] += 1
            elif self.hand.points <= 35:
                self.counts[Counts.Small_Slam.value] += 1
            elif self.hand.points >= 35:
                self.counts[Counts.Grand_Slam.value] += 1
            self.ResetHand()
        self.ConvertOutcomes()
        self.PrintOutcomes(x_times)
    def ConvertOutcomes(self):
        for index, count in enumerate(self.counts):
            self.outcome[index] = (count / self.cycle) * 100
    def PrintOutcomes(self, x_times):
        print("The estimated probability outcome based on", x_times, "simulated hands:")
        for index, prob in enumerate(self.outcome):
            print(self.outcomeNames[index], ": ", end='')
            print('{0:.2f}%'.format(self.outcome[index]))
        print()

