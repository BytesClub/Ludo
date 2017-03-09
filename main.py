import random

class Dice(object):
    def __init__(self):
        self.value = 0
    def roll(self):
        self.value = random.randint(1, 6)
    def getValue(self):
        if self.value == 0:
            raise ValueError('Dice is not been rolled yet!')
        return self.value

class Tunnel(object):
    def __init__(self, diff):
        self.jump = diff
class Snake(Tunnel):
    def jumpValue(self):
        return -1 * self.jump
class Ladder(Tunnel):
    def jumpValue(self):
        return self.jump

class Coin(object):
    def __init__(self, max):
        self.position = 0
        self.maxVal = max
    def getPosition(self):
        return self.position
    def update(self, dice):        
        if dice.getValue() <= 0 or dice.getValue() > 6:
            raise ValueError('Value of Dice should be in range 1 to 6 inclusive')
        if self.getPosition() == 0 and dice.getValue() != 1:
            return None
        self.position += dice.getValue()
    def jump(self, amount):
        if (self.getPosition() + amount) <= 0 or(self.getPosition() + amount) > self.maxVal:
            return None
            # raise ValueError('The Tunnel should reside within the board range')
        self.position += amount

class Board(object):
    def __init__(self, max, num):
        self.minVal = 1
        self.maxVal = max
        self.coin = Coin(max)
        self.tunnels = {}
        for i in range(0, num):
            start = random.randint(1, max)
            stop = random.randint(1, max)
            diff = abs(start - stop)
            if diff == 0:
                continue
            self.tunnels[min(start, stop)] = Ladder(diff) if i % 2 == 0 else Snake(diff)
        # print(self.tunnels) -DEBUG
    def getPosition(self):
        return self.coin.getPosition()
    def update(self, dice):
        self.coin.update(dice)
        if self.coin.getPosition() in self.tunnels:
            self.coin.jump(self.tunnels[self.coin.getPosition()].jumpValue())
    def win(self):
        if(self.getPosition() >= self.maxVal):
            return True
        return False

def main():
    count = 0
    board = Board(100, 10)
    dice = Dice()
    while count < 30:
        dice.roll()
        print('Dice gives:', dice.getValue())
        board.update(dice)
        count += 1
        print('You are in', board.getPosition(), 'position', end = '\n\n')
        if board.win():
            print('Congratulations, You Won!')
            return
    print('Sorry, You lose!')

if __name__ == "__main__":
    main()