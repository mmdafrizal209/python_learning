def balok():
    p = int(input('masukkan nilai panjang: '))
    l = int(input('masukkan nilai luas: '))
    t = int(input('masukkan nilai tinggi: '))

    v = lambda : p * l * t
    print(v())
balok()