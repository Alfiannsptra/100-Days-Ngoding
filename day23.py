while True:
    nilai = int(input("masukkan nilai anda :"))
    
    if nilai >= 90 and nilai <= 100:
        print("nilai anda A")
        break
    elif nilai >= 80 and nilai <= 89:
        print("Nilai anda A-")
        break
    elif nilai >= 70 and nilai <=79:
        print("Nilai anda B")
        break
    elif nilai >= 60 and nilai <=69:
        print("Nilai anda B-")
        break
    elif nilai >=50 and nilai <=59:
        print("Nilai anda C")
        break
    elif nilai>=40 and nilai <=49:
        print("Nilai anda C-")
        break
    elif nilai >= 30 and nilai <= 39:
        print("Nilai anda D")
        break
    elif nilai <= 29:
        print("Nilai Anda E ")
        break
    elif nilai >101:
        print("Nilai anda diluar batas")
        break
    else:
        print("coba Masukkan ulang nilai anda")
        break
                
                    
                    
                
