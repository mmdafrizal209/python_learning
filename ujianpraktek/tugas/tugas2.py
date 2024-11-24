bilangan1 = int(input("Masukkan bilangan pertama: "))
bilangan2 = int(input("Masukkan bilangan kedua: "))
bilangan3 = int(input("Masukkan bilangan ketiga: "))

if bilangan1 > bilangan2:
    bilangan1, bilangan2 = bilangan2, bilangan1  

if bilangan1 > bilangan3:
    bilangan1, bilangan3 = bilangan3, bilangan1  

if bilangan2 > bilangan3:
    bilangan2, bilangan3 = bilangan3, bilangan2  

    print("Bilangan terurut: ", bilangan1, bilangan2, bilangan3)