import random

def tebak_angka():
    angka_rahasia = random.randint(1, 100)
    tebakan = None

    while tebakan != angka_rahasia:
        tebakan = int(input("Tebak angka (1-100): "))

        if tebakan < angka_rahasia:
            print("Terlalu rendah!")
        elif tebakan > angka_rahasia:
            print("Terlalu tinggi!")

    print("Selamat, tebakanmu benar!")

tebak_angka()
