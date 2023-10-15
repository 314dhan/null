from Bayes import Bayes

# Membuat object dari class Bayes dengan nilai-nilai yang diketahui
objek_bayes = Bayes(0.01, 0.05, 0.99)

# Mengakses dan menampilkan nilai-nilai atribut dari object
print("pA =", objek_bayes.pA)
print("pB =", objek_bayes.pB)
print("pBA =", objek_bayes.pBA)

# Mengakses dan menampilkan hasil metode bayes dari object
print("Peluang seseorang menderita penyakit A jika hasil tes positif adalah", round(objek_bayes.bayes(), 3))
