s = ' '
a = float(input("angka awal: "))
r = float(input("rasio: "))
m = int(input("suku awal: "))
k =  int(input(" suku akhir: "))

for n in range (m,k):
    geometry = a * ( r ** (n-1))
    s += str(geometry) + ' '
print(s)


for n in range (m,k):
    sn = a * ( (r ** (n)) - 1 )/ (r-1)

print( "jumlah hasil: ", sn )


print("kodey yang disesuaikan dengan soal 4")
s = ' '                    
for n in range (1,11):
    geometry = 1 * ( 3 ** (n-1))
    s += str(geometry) + ' '
print(s)


for n in range (1,11):
    sn = a * ( (3 ** (n)) - 1 )/ (3-1)

print( "jumlah hasil: ", sn )
