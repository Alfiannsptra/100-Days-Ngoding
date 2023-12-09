from math import sqrt

a = int(input("masukkan nilai a: "))
b = int(input("masukkan nilai b: "))
c = int(input("masukkan nilai c: "))

d = sqrt(b * b - 4 * a * c)
x1 = (-b + d) / (2 * a)
x2 = (-b - d) / (2 * a)

print(x1)
print(x2)
