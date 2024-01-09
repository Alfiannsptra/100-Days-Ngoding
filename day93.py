batas = int(input("masukkan batas: "))
arr = []
jumlah = 0
for i in range(1,batas):
    angka = int(input("masukkan angka: "))
    arr.append(angka)
    jumlah+=angka
print(arr)

if jumlah %2 == 0:
    print(jumlah,"genap")
else:
    print(jumlah,"ganjil")