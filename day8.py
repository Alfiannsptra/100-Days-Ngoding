# Program mengetahui gaji bersih yang diterimakaryawan setiap bulan

# inisialisai gaji pokok dan lama lembur dengan inputan
gaji_pokok = float(input("Masukkan gaji pokok per bulan: "))
lama_lembur = float(input("Masukkan lama lembur per bulan (jam): "))
gaji_lembur_per_jam = 55000

# rumus menghitung gaji bersih setekah ditambah dengan lembur
gaji_lembur = lama_lembur * gaji_lembur_per_jam
gaji_kotor = gaji_pokok + gaji_lembur
gaji_bersih = gaji_kotor

# menampilkan
print("rincian gaji anda")
print("gaji pokok anda  :", gaji_pokok)
print("gaji lembur anda :", gaji_lembur)
print("gaji kotor       :", gaji_kotor)
print("gaji bersih anda :", gaji_bersih)
