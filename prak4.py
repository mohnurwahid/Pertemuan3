n = int(input("Masukkan batas atas (n): "))

print("Bilangan ganjil sampai", n, ":")
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i, end=" ")
