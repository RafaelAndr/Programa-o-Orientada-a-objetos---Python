import random

class RandomTester:
    def __init__(self):
        pass

    def printOneRandom(self):
        num = random.randint(-9999, 9999)
        print(num)

    def printMultiRandom(self, many):
        for i in range(1, many+1):
            self.printOneRandom()

    def throwDice(self):
        num = random.randint(1, 6)
        print(num)

    def max(self, maxNum):
        self.minMax(1, maxNum)

    def minMax(self, minNum, maxNum):
        num = random.randint(minNum, maxNum)
        print(num)