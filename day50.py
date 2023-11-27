batas = int(input("Masukkan angka batas: "))

if angka_batas > 2:
    for i in range(batas + 1):
        if i % 3 == 0:
            print(i)
else:
    print("kosong")

