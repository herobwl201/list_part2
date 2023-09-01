# Đếm số chặn và lẻ trong đoạn [0, 1000] theo 2 cách thông thường và list comprehension

# Cách thông thường 
odd = even = 0
for i in range(0, 1001):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"Số các số lẻ là: {odd}")
print(f"Số các số chẵn là: {even}")

# Cách list comprehension

lst = list(range(0, 1001))

lst_odd = [n for n in lst if n != 2 == 0]
lst_even = [n for n in lst if n % 2 == 0]

print(f"Số các số lẻ là: {len(lst_odd)}")
print(f"Số các số chẵn là: {len(lst_even)}")
