angka_list = input("Masukkan angka-angka (pisahkan dengan spasi): ")
angka_list = list(map(float, angka_list.split()))
rata_rata = sum(angka_list) / len(angka_list)
print(f"Rata-rata dari angka-angka tersebut adalah {rata_rata}.")