panjang_m = float(input("Masukkan panjang benda dalam meter: "))

panjang_inchi = panjang_m * 1000 / 25.4
panjang_kaki = panjang_m * 100 / 30.48
panjang_yard = panjang_m / 0.9144

print(f"Panjang dalam inchi: {panjang_inchi:.2f} inchi")
print(f"Panjang dalam kaki: {panjang_kaki:.2f} kaki")
print(f"Panjang dalam yard: {panjang_yard:.2f} yard")