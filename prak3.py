n = int(input("Masukkan batas atas (n): "))

a, b = 0, 1
print("Deret Fibonacci sampai", n, ":")
while a <= n:
    print(a, end=" ")
    a, b = b, a + b
