menu_kopi = {}

def tambah_menu():
    nama = input("Masukkan nama menu: ")
    harga = int(input("Masukkan harga menu: "))
    menu_kopi[nama] = harga
    print("Menu " + nama + " ditambahkan dengan harga Rp" + str(harga) + ".")

def lihat_menu():
    print("Daftar Menu Warung Kopi:")
    for nama, harga in menu_kopi.items():
        print(nama + ": Rp" + str(harga))

def update_menu():
    nama = input("Masukkan nama menu yang akan diupdate: ")
    if nama in menu_kopi:
        harga = int(input("Masukkan harga baru: "))
        menu_kopi[nama] = harga
        print("Menu " + nama + " diperbarui dengan harga Rp" + str(harga) + ".")
    else:
        print("Menu " + nama + " tidak ditemukan.")

def hapus_menu():
    nama = input("Masukkan nama menu yang akan dihapus: ")
    if nama in menu_kopi:
        del menu_kopi[nama]
        print("Menu " + nama + " dihapus.")
    else:
        print("Menu " + nama + " tidak ditemukan.")

while True:
    print("\n=== Aplikasi Warung Kopi ===")
    print("1. Tambah Menu")
    print("2. Lihat Menu")
    print("3. Update Menu")
    print("4. Hapus Menu")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan (1-5): ")

    if pilihan == "1":
        tambah_menu()
    elif pilihan == "2":
        lihat_menu()
    elif pilihan == "3":
        update_menu()
    elif pilihan == "4":
        hapus_menu()
    elif pilihan == "5":
        print("Terima kasih, program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan angka 1-5.")
