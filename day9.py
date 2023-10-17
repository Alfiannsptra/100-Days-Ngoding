# Perulangan while 
while True:
    #menu pilihan
    print("laptop")
    print("1. asus")
    print("2. acer")
    print("3. Keluar")

    #masukkan pilihan
    pilihan = input("Masukkan pilihan Anda: ")

    #kondisi
    if pilihan == "1":
        print("anda memilih laptop asus")
    elif pilihan == "2":
        print("Anda memilih laptop acer")
    elif pilihan == "3":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        
