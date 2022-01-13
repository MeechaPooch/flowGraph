import units
import random

class Connection:

    def __init__(self, fro, to, rate):
        self.fro = fro
        self.to = to
        self.rate = rate
        self.takeVal = None
        self.randVal = random.random()
        # self.rateRule = lambda t:t*self.rate
        self.val = 0

    def calcTake(self):
        # self.takeVal = self.rateRule(self.fro.val)
        self.takeVal = self.fro.val * self.rate

    def transfer(self,deltaTime):
        timedVal = self.takeVal * deltaTime/units.timeUnit
        self.fro.val -= timedVal
        self.to.val += timedVal
        