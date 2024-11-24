x = int(input("Masukkan bilangan bulat x: "))
y = int(input("Masukkan bilangan bulat y: "))
z = int(input("Masukkan bilangan bulat z: "))

temp = x

x = y
y = z
z = temp

print(f"Hasil pertukaran: x = {x}, y = {y}, z = {z}")