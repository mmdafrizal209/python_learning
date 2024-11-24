def konversi_hari(z):
    tahun = z // 365
    sisa_hari = z % 365
    bulan = sisa_hari // 30
    hari = sisa_hari % 30
    
    return tahun, bulan, hari

z = int(input("Masukkan jumlah hari proyek: "))

tahun, bulan, hari = konversi_hari(z)

print(f"Proyek dikerjakan selama: {tahun} tahun, {bulan} bulan, {hari} hari")