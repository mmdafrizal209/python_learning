uang = int(input("Masukkan nilai uang dalam rupiah (kelipatan 25): "))

pecahan_1000 = 0
pecahan_500 = 0
pecahan_100 = 0
pecahan_50 = 0
pecahan_25 = 0

if uang >= 1000:
    pecahan_1000 = uang // 1000
    uang = uang % 1000

if uang >= 500:
    pecahan_500 = uang // 500
    uang = uang % 500

if uang >= 100:
    pecahan_100 = uang // 100
    uang = uang % 100

if uang >= 50:
    pecahan_50 = uang // 50
    uang = uang % 50

if uang >= 25:
    pecahan_25 = uang // 25
    uang = uang % 25

print(f"Pecahan Rp1000: {pecahan_1000}")
print(f"Pecahan Rp500: {pecahan_500}")
print(f"Pecahan Rp100: {pecahan_100}")
print(f"Pecahan Rp50: {pecahan_50}")
print(f"Pecahan Rp25: {pecahan_25}")