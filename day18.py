#menghitung jumlah karakter pada suatu kata
def hitungKarakter(kata):
    jumlah = 0
    for karakter in kata:
        jumlah += 1
    return jumlah

# masukkan kata
kata = input("Masukkan suatu kata: ")

# Memanggil fungsi dan menampilkan hasil
jumlahKarakter = hitungKarakter(kata)
print("Jumlah karakter dalam kata",kata,":",jumlahKarakter)

#note : jika terdapat spasi pada penginputan kata maka terhitung 1
