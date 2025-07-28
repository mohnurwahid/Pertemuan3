persentase = float(input("Masukkan persentase nilai siswa: "))

if persentase >= 90:
    print("Performa: Sangat Baik (Excellent)")
elif persentase >= 80:
    print("Performa: Baik Sekali (Very Good)")
elif persentase >= 70:
    print("Performa: Baik (Good)")
elif persentase >= 60:
    print("Performa: Cukup (Average)")
else:
    print("Performa: Perlu Perbaikan")