# Nhập hai số a và b từ bàn phím, in ra số lớn nhất và nhỏ nhất trong hai số
a = float(input("Nhập vào a: "))
b = float(input("Nhập vào b: "))

s = 'a là số lớn nhất'
if a < b:
    s = ("b là số lớn nhất")
print(s)