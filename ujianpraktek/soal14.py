inputhuruf = input("masukan huruf: ")

vokal = ('a', 'i', 'u', 'e', 'o')
konsonan = ('b', 'd', 'c', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')

bukankeduanya = True

for i in vokal:
    if inputhuruf. lower().strip() ==i:
        print(inputhuruf, "adalah vokal")
        bukankeduanya = False

for i in konsonan:
    if inputhuruf.lower().strip() ==i:
        print(inputhuruf,"adalah konsonan")
        bukankeduanya = False 

if bukankeduanya:
 print(inputhuruf, "bukan keduanya")