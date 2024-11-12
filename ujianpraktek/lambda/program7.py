def segitiga():
    phi = 0.5

    alas = int(input('masukkan nilai alas: '))
    tinggi = int(input('masukkan nilai tinggi: '))

    l = lambda : phi * alas * tinggi
    print(l())
segitiga()