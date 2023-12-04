namaKota = ["Jakarta", "Bandung", "Surabaya", "Yogyakarta", "Semarang", "Medan","Majene", "Denpasar"]

cariKota = input("Masukkan huruf pertama kota yang ingin dicari: ")

kotaTerpenuhi = []
for kota in namaKota:
    if kota.startswith(cariKota):
        kotaTerpenuhi.append(kota)

print("Nama kota yang anda cari:")
for kota in kotaTerpenuhi:
    print(kota)
