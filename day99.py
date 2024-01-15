import random

batas_bawah = int(input("Masukkan batas bawah nilai acak: "))
batas_atas = int(input("Masukkan batas atas nilai acak: "))
jumlah_nilai = int(input("Masukkan jumlah nilai acak yang diinginkan: "))

nilai_acak = []

for _ in range(jumlah_nilai):
    nilai = random.randint(batas_bawah, batas_atas)
    nilai_acak.append(nilai)

print("Nilai acak yang dihasilkan:", nilai_acak)