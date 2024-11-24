def konversi_suhu():
    suhu = float(input("Masukkan suhu: "))
    pilihan = input("Konversi ke (C/F): ").upper()
    
    if pilihan == 'C':
        hasil = (suhu - 32) * 5/9
        print(f"Suhu dalam Celsius: {hasil:.2f}°C")
    elif pilihan == 'F':
        hasil = (suhu * 9/5) + 32
        print(f"Suhu dalam Fahrenheit: {hasil:.2f}°F")
    else:
        print("Pilihan tidak valid!")

konversi_suhu()