def segitiga_sama_kaki():
    phi = 1/2

    alas = int(input('masukkan alas: '))
    tinggi =int(input('masukkan tinggi: '))

    l = lambda : phi * alas * tinggi
    print(l())
segitiga_sama_kaki()