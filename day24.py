def km_ke_mil(kilometer):
    mil = kilometer * 0.621371
    return mil

#menampilkan
km_input= float(input("Masukkan jumlah kilometer: "))
hasil = km_ke_mil(km_input)

print(km_input,"kilometer sama dengan :",hasil,"mil")
