while True:
    a = int(input("Masukkan nilai A: "))
    b = int(input("Masukkan nilai b: "))
    if a < b:
        a,b = b,a
    else:
        for m in range(a,b):
            print(m)
    for s in range(b,a):
        print(s)
