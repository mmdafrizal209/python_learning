angka = int(input("Masukkan angka: "))
jumlah_digit = 0

while angka > 0:
    angka //= 10
    jumlah_digit += 1

print("Jumlah digit:", jumlah_digit)