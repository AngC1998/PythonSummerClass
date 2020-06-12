class Poker:
    def __init__(self, cash):
        self.cash = cash
    def numYellow(self):
        yellowChips = int(self.cash / 1000)
        self.cash = self.cash - (yellowChips * 1000)
        return yellowChips
    def numPurple(self):
        purpleChips = int(self.cash / 500)
        self.cash = self.cash - (purpleChips * 500)
        return purpleChips
    def numBlack(self):
        blackChips = int(self.cash / 100)
        self.cash = self.cash - (blackChips * 100)
        return blackChips
    def numBlue(self):
        blueChips = int(self.cash / 50)
        self.cash = self.cash - (blueChips * 50)
        return blueChips
    def numGreen(self):
        greenChips = int(self.cash / 25)
        self.cash = self.cash - (greenChips * 25)
        return greenChips
    def numRed(self):
        redChips = int(self.cash / 5)
        self.cash = self.cash - (redChips * 5)
        return redChips
    def numWhite(self):
        return self.cash

cash = int(input("Cash: $"))
player = Poker(cash)
yellow_chips = player.numYellow()
print("yellow chips: "+str(yellow_chips))
purple_chips = player.numPurple()
print("purple chips: "+str(purple_chips))
black_chips = player.numBlack()
print("black chips: "+str(black_chips))
blue_chips = player.numBlue()
print("blue chips: "+str(blue_chips))
green_chips = player.numGreen()
print("green chips: "+str(green_chips))
red_chips = player.numRed()
print("red chips: "+str(red_chips))
white_chips = player.numWhite()
print("white chips: "+str(white_chips))