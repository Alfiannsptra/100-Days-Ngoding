import random

nomor_rahasia = random.randint(1, 100)
maksimal_percobaan = 5
percobaan = 0

print("Halo! Saya telah memilih sebuah angka antara 1 dan 100. Coba tebak!")

while percobaan < maksimal_percobaan:
    tebakan = input("Masukkan tebakan anda: ")
    
    if not tebakan.isdigit():
        print("Maaf, harap masukkan angka.")
        continue

    tebakan = int(tebakan)
    
    if tebakan == nomor_rahasia:
        print("Selamat! Anda berhasil menebak angka", nomor_rahasia, "dalam", percobaan + 1, "percobaan.")
        break
    elif tebakan < nomor_rahasia:
        print("Terlalu rendah! Coba lagi.")
    else:
        print("Terlalu tinggi! Coba lagi.")

    percobaan += 1

if percobaan == maksimal_percobaan:
    print("Sayang sekali! Anda sudah menggunakan semua percobaan. Angka yang benar adalah", nomor_rahasia, ".")
