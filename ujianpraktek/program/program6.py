def hitung_jarak_tanggal(tanggal1, tanggal2):

    hari1, bulan1, tahun1 = map(int, tanggal1.split(':'))
    hari2, bulan2, tahun2 = map(int, tanggal2.split(':'))
    
    total_hari1 = (tahun1 * 365) + (bulan1 * 30) + hari1
    total_hari2 = (tahun2 * 365) + (bulan2 * 30) + hari2
    
    selisih_hari = abs(total_hari1 - total_hari2)
    
    tahun = selisih_hari // 365
    sisa_hari = selisih_hari % 365
    bulan = sisa_hari // 30
    hari = sisa_hari % 30
    
    return tahun, bulan, hari

tanggal1 = input("Masukkan tanggal pertama (dd:mm:yy): ")
tanggal2 = input("Masukkan tanggal kedua (dd:mm:yy): ")


tahun, bulan, hari = hitung_jarak_tanggal(tanggal1, tanggal2)


print(f"Jarak antara kedua tanggal: {tahun} tahun, {bulan} bulan, {hari} hari")