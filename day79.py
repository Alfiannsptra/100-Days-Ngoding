def tambah_ganjil_genap(batas):
    array_angka = []

    for i in range(batas):
        angka = int(input(f"Masukkan angka ke-{i + 1}: "))
        array_angka.append(angka)

    jumlah_ganjil = 0
    jumlah_genap = 0

    for angka in array_angka:
        if angka % 2 != 0:
            jumlah_ganjil += angka
        else:
            jumlah_genap += angka

    print("Array angka:", array_angka)
    print("Jumlah angka ganjil:", jumlah_ganjil)
    print("Jumlah angka genap:", jumlah_genap)

batas = int(input("Masukkan batas: "))
tambah_ganjil_genap(batas)
