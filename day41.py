arr = []
while True:
	print("CRUD")
	print("1. Tambah data")
	print("2. Hapus data ")
	print("3. EXIT")
	pilih = int(input("masukkan pilihan: "))
	if pilih == 1:
		tambah = int(input("tambahkan data: "))
		arr.append(tambah)
		print(arr)
	elif pilih == 2 :
		hapus = int(input("Hapus data: "))
		arr.remove(hapus)
		print(arr)
	elif pilih == 3:
		print("Terima Kasih")
		print(arr)
		break