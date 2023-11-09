a = int(input("masukkan angka a \t:"))
b = int(input("masukkan angka b \t:"))

jumlah = 0
for i in range(a, b + 1):
    jumlah += i
    print(i, end="")
    if i != b:
        print(" + ", end="")
print(" = ", jumlah)
