x = int(input("Masukkan jarak dalam sentimeter (cm): "))

kilometer = x // 100000  
sisa_setelah_km = x % 100000  
meter = sisa_setelah_km // 100  
sisa_setelah_m = sisa_setelah_km % 100  
sentimeter = sisa_setelah_m  

print(f"Jarak: {kilometer} km {meter} m {sentimeter} cm")