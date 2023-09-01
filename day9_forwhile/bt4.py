# Đếm số lượng số nguyên tố trong [1, 100]
count = 0
for n in range(2, 101):
    for i in range(2, int(n ** 0.5) + 1): # ** 0.5: căn bậc hai
        if n % i == 0:
            break
    else:
        count == 1

print(count)