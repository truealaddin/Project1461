from Card import Card

class Hand:
    def __init__(self):
        self.cards = []
        self.points = 0

    def AddCard(self, cardValue):
        card = Card(cardValue)
        self.cards.append(card)
        if (len(self.cards) > 13):
                print("There are only 13 cards in a hand")
                exit()

    def HighCard(self):
        for c in self.cards:
            if c.cardValue() == "A":
                self.points += 4
            elif c.cardValue() == "K":
                self.points += 3
            elif c.cardValue() == "Q":
                self.points += 2
            elif c.cardValue() == "J":
                self.points += 1

    def Distribution(self):
        s,h,d,c = 0, 0, 0, 0
        for card in self.cards:
            if card.cardSuit() == 'S':
                s += 1
            elif card.cardSuit() == 'H':
                h += 1
            elif card.cardSuit() == 'D':
                d += 1
            elif card.cardSuit() == 'C':
                c += 1
        cardSuits = [s, h, d, c]
        for suit in cardSuits:
            if suit == 2:
                self.points += 1
            elif suit == 1:
                self.points += 2
            elif suit == 0:
                self.points += 5
    def PrintHand(self):
        print(*self.cards, sep=", ")
    def PrintPoints(self, ):
        print("Here is your hand:")
        self.CalculatePoints()
        print(f'This hand is worth {self.points} points')
    def PrintInfo(self):
        self.PrintHand()
        self.PrintPoints()

    def CalculatePoints(self, otherPoints = 0):
        self.HighCard()
        self.Distribution()
        self.points += otherPoints





