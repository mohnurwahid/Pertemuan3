a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))
c = float(input("Masukkan angka ketiga: "))

if a >= b and a >= c:
    print("Angka terbesar adalah:", a)
elif b >= a and b >= c:
    print("Angka terbesar adalah:", b)
else:
    print("Angka terbesar adalah:", c)