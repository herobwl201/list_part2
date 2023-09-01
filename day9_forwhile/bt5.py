# Nhập vào số nguyên dương n, tính tổng các chữ số của n. Ví dụ: n = 4312 => 5 = 4 + 3 +1 +2 = 10

n = int(input("n = "))

while n <= 0:
    print("n không phải là số nguyên dương")
    n = int(input("n = "))

s = 0

while n > 0:
    last = n % 10
    s += last
    n //= 10

print(s)