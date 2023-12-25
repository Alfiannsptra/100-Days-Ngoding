batas = int(input("masukkan batas: "))
jumlah =0
for i in range(1,batas):
	if i% 2== 0:
		print(i,"ml game stress")
	elif i%2!= 0:
		print(i,"pubg ajaa")
	jumlah+=i
print("jumlah =",jumlah)