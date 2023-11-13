angka = int(input("masukkan angka: "))
totalGenap = 0
totalGanjil = 0
for i in range (1,angka):
    if i % 2 == 0:
        print("nilai: ",i)
        totalGenap+=i
print(totalGenap)

for i in range (1,angka+1):
    if i % 2 != 0:
        print("nilai: ",i)
        totalGenap+=i
print(totalGanjil)
     
        
