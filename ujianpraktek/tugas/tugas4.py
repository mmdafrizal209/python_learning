def hitung_rata_rata():
    jumlah = int(input("Masukkan jumlah angka: "))
    total = 0
    for _ in range(jumlah):
        angka = float(input("Masukkan angka: "))
        total += angka
    rata_rata = total / jumlah
    print(f"Rata-rata: {rata_rata}")

hitung_rata_rata()