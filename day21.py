nama = input("Masukkan nama anda :")
if nama == "alfian":
    nilai = int(input("Masukkan nilai Anda: "))
    batas = int(input("masukkan nilai batas :"))
    for i in range(nilai,batas):
        print(i)
        if i == 20:
            print("berhenti")
            break
else:
    print("nama tidak ada")

