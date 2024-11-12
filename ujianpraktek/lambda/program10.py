def prisma():
    phi = 1/2

    p = int(input('masukkan nilai panjang: '))
    l = int(input('masukkan nilai luas: '))
    t = int(input('masukkan tinggi: '))

    v = lambda : phi * p * l * t
    print(v())
prisma()