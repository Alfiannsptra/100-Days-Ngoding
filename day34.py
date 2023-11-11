arr = []
jumlah = 0
for i in range(0, 10):
    isi = int(input("masukkan nilai :"))
    arr.append(isi)
    print(arr)
print(arr[1])
print(arr[7])
print(arr[9])

print("sebelum di hapus :", arr)
del (arr[4])
del (arr[8])
print("sesudah di hapus :", arr)

arr[3] = 20
print("update nilai pada index ke 3 :", arr)
