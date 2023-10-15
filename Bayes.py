# Mendefinisikan class Bayes
class Bayes:
    # Mendefinisikan konstruktor
    def __init__(self, pA, pB, pBA):
        # Menginisialisasi atribut
        self.pA = pA
        self.pB = pB
        self.pBA = pBA

    # Mendefinisikan metode bayes
    def bayes(self):
        # Menghitung dan mengembalikan peluang bersyarat
        return self.pA * self.pBA / self.pB

