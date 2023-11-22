penghasilan = float(input("Masukkan penghasilan: "))
jenis_pekerjaan = input("Masukkan jenis pekerjaan: ")

pajak = 0

if penghasilan >= 5000000:
    print("kena pajak 10%")
    pajak += 10
elif penghasilan >= 3000000:
    print("kena pajak 5%")
    pajak += 5

if jenis_pekerjaan== "pns":
    print("tambahan pajak 5%")
    pajak += 5

penghasilan_bersih = penghasilan - (penghasilan * (pajak / 100))

print("Penghasilan bersih setelah dipotong pajak:", penghasilan_bersih, "juta")
