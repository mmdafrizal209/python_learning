N = int(input("Masukkan angka N: "))
print("Bilangan genap dari 1 sampai", N, "adalah:")
for i in range(1, N + 1):
    if i % 2 == 0:
        print(i)