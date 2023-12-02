batas = int(input("masukkan batas: "))
arr = []
jumlah = 0

for i in range(1, batas):
    isi = int(input("masukkan angka: "))
    arr.append(isi)
    jumlah += isi

print(arr)
print(jumlah)

rataRata = jumlah / (batas - 1)
print("Rata-rata: ",rataRata)
