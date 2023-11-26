try:
    a = int(input("masukkan nilai a: "))
    b = int(input("masukkan nilai b: "))
    print("hasil a/b adalah: ",a/b)
except ZeroDivisionError:
    print("masukkan angka selain 0")
    
#pada python exception bisa di atasi dengan try except statement. dimana kode yang berpotensi menimbulkan exception/error kita masukkan ke dalam blok try, dan pada blok except dimasukkan kode yang akan dieksekusi saat terjadi error.