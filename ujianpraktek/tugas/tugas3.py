a = int(input("Masukkan panjang sisi a: "))
b = int(input("Masukkan panjang sisi b: "))
c = int(input("Masukkan panjang sisi c: "))

sisi = sorted([a, b, c])
a = sisi[0]
b = sisi[1]
c = sisi[2]

a_squared = a ** 2
b_squared = b ** 2
c_squared = c ** 2

if a_squared + b_squared == c_squared:
    print("Segitiga tersebut adalah segitiga siku-siku.")
elif a_squared + b_squared > c_squared:
    print("Segitiga tersebut adalah segitiga lancip.")
else:
    print("Segitiga tersebut adalah segitiga tumpul.")
