batas = int(input("masukkan batas: "))
arr = []
jumlah = 0
for i in range(1,batas):
    angka = int(input("masukkan angka: "))
    arr.append(angka)
    jumlah+=angka
print(arr)
print(jumlah)