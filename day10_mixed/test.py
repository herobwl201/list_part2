# Tạo ra list mới chứa các giá trị mũ 3 dựa trên cái list ban đầu
lst = [1, 2, 3, 4]

# Cách 1: list comprehensions
new_lst = [v**3 for v in lst]

print(new_lst)

# Cách 2: cách dài dòng
new_lst = []

for x in lst:
    new_lst.append(x**3)
print(new_lst)

# vd khác
numbers = [100, 34, 56, 78, 80, -46, 3, 5, -11]
# Tính tổng các số lẻ có trong list
new_lst = [v for v in numbers if v % 2 != 0]
print(new_lst)
print(sum(new_lst))

# vd lấy giá trị chẵn * 2 và giá trị lẻ * 3
numbers = [100, 34, 56, 78, 80, -46, 3, 5, -11]

new_lst = [v*2 if v % 2 == 0 else v * 3 for v in numbers]
print(new_lst)
# Cách 2:
new_lst = []

for x in numbers:
    if x % 2 == 0:
        new_lst.append(x * 2)
    else:
        new_lst.append(x*3)
print(new_lst)

# zip
# enumerate

lst = {1, 2, 3, 4}

# {i} - {value}
# enumerate
for item in enumerate(lst, start=1):
    idx, value = item
    print(f"{idx} - {value}")

# zip
print(list(zip(enumerate(lst, start=1))))

#
print(list(range(len(lst)))) # len(lst) = 4, range(len(lst)) tính từ 0 -> 3

for i in range(len(lst)):
    print(i, lst[i]) # truy cập giá trị tại vị trí là i

for i in range(len(lst)):
    if i % 2 == 0: # tìm vị trí lẻ
        print(i, lst[i]) # truy cập giá trị tại vị trí là i


for i, v in enumerate(lst):
    if i % 2 != 0:
        print(i, v)