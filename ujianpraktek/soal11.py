print('*'*48)
jumlah = int(input('masukan total harga : '))
print('*'*48)

diskon = 0
if jumlah >= 10000000:
    diskon = 5 * jumlah
    total_harga = jumlah - diskon 
    print("diskon yang di dapat : ", diskon)
    print("total harga yang harus di bayar : ", total_harga)
elif jumlah <= 100000:
    print("total harga : ",jumlah)