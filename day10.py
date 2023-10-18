while True:
    # menu pilihan
    print("ARITMATIKA")
    print("1. Penjumlahan")
    print("2. Perkalian")
    print("3. Pengurangan")
    print("4. Pembagian")
    print("5. EXIT")

    # masukkan pilihan
    pilihan = int(input("Masukkan pilihan Anda: "))

    # kondisi
    if pilihan == 1:
        print("PENJUMLAHAN")
        angka1 = int(input("masukkan angka pertama :"))
        angka2 = int(input("masukkan angka kedua   :"))
        penjumlahan = angka1 + angka2
        print("Penjumlahan,", angka1, "+", angka2, "adalah :", penjumlahan)
    elif pilihan == 2:
        print("PERKALIAN")
        angka1 = int(input("masukkan angka pertama :"))
        angka2 = int(input("masukkan angka kedua   :"))
        perkalian = angka1 * angka2
        print("Perkalian,", angka1, "*", angka2, "adalah :", perkalian)
    elif pilihan == 3:
        print("PENGURANGAN")
        angka1 = int(input("masukkan angka pertama :"))
        angka2 = int(input("masukkan angka kedua   :"))
        pengurangan = angka1 - angka2
        print("Pengurangan,", angka1, "-", angka2, "adalah :", pengurangan)
    elif pilihan == 4:
        print("PEMBAGIAN")
        angka1 = int(input("masukkan angka pertama :"))
        angka2 = int(input("masukkan angka kedua   :"))
        pembagian = angka1 / angka2
        print("Pembagian,", angka1, "/", angka2, "adalah :", pembagian)
    elif pilihan == 5:
        print("Terima kasih Telah menggunakan Program ARITMATIKA kami")
        break
    else:
        print("Opsi yang anda pilih tidak ada. Coba lagi")
