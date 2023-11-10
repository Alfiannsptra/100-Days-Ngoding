def batasan(x):
    arr = []
    jumlah = 0
    while True:
        a = int(input("masukkan nilai x:"))
        arr.append(x)
        jumlah += a
        print(arr, "=", jumlah)
        if jumlah >= x:
            print("berhenti")
            break
print(batasan(20))
