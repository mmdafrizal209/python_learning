angka = int(input("Masukkan angka: "))
faktorial = 1

for i in range(1, angka + 1):
    faktorial *= i

print(f"Faktorial dari {angka} adalah {faktorial}")