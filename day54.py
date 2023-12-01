batas = int(input("Masukkan batas angka: "))

angkaGanjil = []
angkaGenap = []

for angka in range(1, batas + 1):
    if angka % 2 == 0:
        angkaGenap.append(angka)
    else:
        angkaGanjil.append(angka)

semua_angka = angkaGanjil + angkaGenap

print("Semua Angka:", semua_angka)
