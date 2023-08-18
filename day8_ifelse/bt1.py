# Nhập vào một số nguyên n, kiểm tra và in n là số chẵn hay lẻ
n = int(input("Nhập vào số n: "))
if n % 2 == 0:
    print("n là số chẵn")
else:
    print("n là số lẻ")

# Cách 2
n = int(input("Nhập vào số n: "))

s = "n là số chẵn"

if n % 2 != 0:
    s = "n là số lẻ"

print(s)