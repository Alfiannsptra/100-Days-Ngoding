batas = int(input("Masukkan batas angka: "))

angkaGanjil = []
angkaGenap = []

for angka in range(1, batas + 1):
    if angka % 2 == 0:
        angkaGenap.append(angka)
    else:
        angkaGanjil.append(angka)

print("Angka Ganjil:")
for ganjil in angkaGanjil:
    print(ganjil,"ganjil")

print("Angka Genap:")
for genap in angkaGenap:
    print(genap,"genap")
