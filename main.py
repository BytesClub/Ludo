import random

class Dice(object):
	def __init__(self):
		self.value = 0
	def roll(self):
		self.value = random.randint(1, 6)
	def getValue(self):
	    return self.value

class Tunnel(object):
    def __init__(self):
        self.jump = random.randint(1, 100)

class Snake(Tunnel):
    def jumpValue(self):
        return -1 * self.jump

class Ladder(Tunnel):
    def jumpValue(self):
        return self.jump

class Coin(object):
    def __init__(self):
        self.position = 0
    def getPosition(self):
        return self.position
    def update(self, dice):
        if dice.getValue() <= 0 or dice.getValue() > 6:
            raise ValueError('Value of Dice should be in range 1 to 6 inclusive')
        self.position += dice.getValue()
    def jump(self, amount):
        if (self.getPosition() + amount) <= 0 or (self.getPosition() + amount) > 100:
            return None
            # raise ValueError('The Tunnel should reside within the board range')
        self.position = amount

class Board(object):
    def __init__(self):
        self.minVal = 1
        self.maxVal = 100
        self.coin = Coin()
        self.tunnels = {}
        for i in range(0, 10):
            position = random.randint(1, 100)
            while position in self.tunnels:
                continue
            self.tunnels[position] = Ladder() if i % 2 == 0 else Snake()
    def getPosition(self):
        return self.coin.getPosition()
    def update(self, dice):
        self.coin.update(dice)
        if self.coin.getPosition() in self.tunnels:
            self.coin.jump(self.tunnels[self.coin.getPosition()].jumpValue())

def main():
    count = 0
    board = Board()
    dice = Dice()
    while count < 5:
        dice.roll()
        board.update(dice)
        count += 1
        print('You are in', board.getPosition(),'position');
        if board.getPosition() == 100:
            print('Congratulations, You Won!')
            return
    print('Sorry, You lose!')

if __name__ == "__main__":
    main()