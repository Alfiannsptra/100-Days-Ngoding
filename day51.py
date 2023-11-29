batas_angka = int(input("Masukkan batas angka: "))

if batas_angka % 2 == 0:
    print("Angka genap")
else:
    print("Angka ganjil:")
    for i in range(1, batas_angka + 1, 2):
        print(i)
