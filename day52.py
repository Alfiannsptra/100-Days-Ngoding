nama = input("Masukkan nama mahasiswa: ")
nim = input("Masukkan NIM mahasiswa: ")
tinggi_badan = float(input("Masukkan tinggi badan: "))
ukuran_baju = input("Masukkan ukuran baju: ")
status_pernikahan = input("Mahasiswa sudah menikah?: ").capitalize() == 'True'
agama = input("Masukkan agama mahasiswa: ")


print("\nData Diri Mahasiswa:")
print("Nama:", nama)
print("NIM:", nim)
print("Tinggi Badan:", tinggi_badan, "Kg")
print("Ukuran Baju:", ukuran_baju)
print("Status Pernikahan:", "Sudah Menikah" if status_pernikahan else "Belum Menikah")
print("Agama:", agama)
