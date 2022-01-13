class Bucket:
    def __init__(self):
        self.val = 0

    def tick(self):
        pass

class ConstantBucket(Bucket):
    def __init__(self, ammount):
        self.amm = ammount
        self.val = ammount

    def tick(self):
        self.val = self.amm