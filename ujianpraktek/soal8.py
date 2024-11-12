print('*'*48)
print('\t\t\PROGRAMING TABUNG')
print("*"*48)

r= int(input('masukan nilai jari-jari\t:'))
tinggi = int (input('masukan nilai tinggi\t:'))

volume = 3.14 * r * r * tinggi
Ip = 2 * 3.14
AA = r + tinggi

print('volume\t\t:',volume,'cm2')
print('Luas permukaan\t\t:' ,Ip * AA, 'cm2')