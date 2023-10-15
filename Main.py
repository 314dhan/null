from Bayes import Bayes as by

class Main:
    print("masukan nilai pA: ")
    pA = float(input())
    print("masukan nilai pB: ")
    pB = float(input())
    print("masukan nilai pBA: ")
    pBA = float(input())
    print("masukan nilai pBnA: ")
    pBnA = float(input())

    objek_bayes = by(pA, pB, pBA, pBnA)

    # Mengakses dan menampilkan nilai-nilai atribut dari object
    print("pA =", objek_bayes.pA)
    print("pB =", objek_bayes.pB)
    print("pBA =", objek_bayes.pBA)
    print("pBA =", objek_bayes.pBnA)

    # Mengakses dan menampilkan hasil metode bayes dari object
    print("Peluang seseorang menderita penyakit A jika hasil tes positif adalah", round(objek_bayes.bayes(), 3))
