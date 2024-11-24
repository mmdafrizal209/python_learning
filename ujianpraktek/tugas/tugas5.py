def cek_genap_ganjil():
    angka = int(input("Masukkan angka: "))
    if angka % 2 == 0:
        print(f"{angka} adalah bilangan genap.")
    else:
        print(f"{angka} adalah bilangan ganjil.")

cek_genap_ganjil()