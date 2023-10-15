# Mendefinisikan class Bayes
class Bayes:

    def __init__(self, pA, pB, pBA, pBnA):
        self.pA = pA
        self.pB = pB
        self.pBA = pBA
        self.pBnA = pBnA

    def bayes(self):
        return self.pA * self.pBA / (self.pA * self.pBA + (1 - self.pA) * self.pBnA)

