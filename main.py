from Hand import Hand
from Deck import Deck
from Simulator import Simulator

if __name__ == '__main__':

    playNum = 500
    cardNum = 13
    response = "y"

    while (response.lower() == 'y'):
        hand = Hand()
        deck = Deck()

        for _ in range(cardNum):
            hand.AddCard(deck.DealCard())

        simulator = Simulator(deck.GetCurrentDeck())
        hand.PrintInfo()

        simulator.RunSimulation(playNum, hand.points)
        response= input("Would You Like Another Hand[y/n]?")

    print("-->Program Exiting<--")