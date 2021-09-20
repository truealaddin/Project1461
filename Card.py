class Card:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    def getVal(self):
        return self.value

    def cardSuit(self):
        return self.value[-1]

    def cardValue(self):
        return self.value[0]