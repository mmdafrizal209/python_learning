import random

def tebak_angka():
    angka_rahasia = random.randint(1, 100)
    tebakan = None
    jumlah_tebakan = 0

    print("Selamat datang di permainan Tebak Angka!")
    print("Saya telah memilih angka antara 1 dan 100.")
    print("Coba tebak angka tersebut!")

    while tebakan != angka_rahasia:
        tebakan = int(input("Masukkan tebakan Anda: "))
        jumlah_tebakan += 1

        if tebakan < angka_rahasia:
            print("Tebakan Anda terlalu rendah. Coba lagi!")
        elif tebakan > angka_rahasia:
            print("Tebakan Anda terlalu tinggi. Coba lagi!")
        else:
            print(f"Selamat! Anda telah menebak angka {angka_rahasia} dengan {jumlah_tebakan} tebakan.")

tebak_angka()