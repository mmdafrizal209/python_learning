tinggi_badan = float(input("Masukkan tinggi badan Anda (dalam cm): "))

pengurangan_pertama = tinggi_badan - 100

sepuluh_persen = 0.1 * pengurangan_pertama

berat_badan_ideal = pengurangan_pertama - sepuluh_persen

print(f"Berat badan ideal untuk tinggi badan {tinggi_badan} cm adalah {berat_badan_ideal:.2f} kg.")