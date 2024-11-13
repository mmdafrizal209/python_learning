jumlah_angka = int(input("Berapa banyak angka yang ingin Anda masukkan? "))
total = 0

for i in range(jumlah_angka):
    angka = float(input(f"Masukkan angka ke-{i + 1}: "))
    total += angka

rata_rata = total / jumlah_angka
print(f"Rata-rata dari {jumlah_angka} angka yang dimasukkan adalah {rata_rata:.2f}.")