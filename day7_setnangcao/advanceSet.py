'''
+ Advanced Set
+ sum, len, min, max, join
'''

set1 = {1, 4, 3, 2}
set2 = {2, 3, 10, -10}
set6 = {10, 11, 20}

# tìm phần chung của set1 và set2
# intersection: giao || giao set1 và set2 lại với nhau
set3 = set1.intersection(set2) # trả về set3 khác set1 và set2
print(set3)

print(set1 & set2) # = intersection, chỉ dùng đc với set

# tìm phần tử nằm trong set1 nhưng không có ở set2
set4 = set1.difference(set2)
print(set4)

print(set1 - set2) # = difference, in ra phần tử nằm trong set1 không nằm trong set2
print(set2 - set1) # = difference, in ra phần tử nằm trong set2 không nằm trong set1

set5 = set2.difference(set1) #in ra phần tử nằm trong set2 không nằm trong set1
print(set5)
# lấy ra tất cả phần tử từ set1 và set2 (union), lấy ra không lặp lại khi trong 2 set đều có giá trị đó
set6 = set1.union(set2)
print(set6)


# toán tử
print(set1 | set2 | set6) # |: dấu pipe, lấy ra tất cả phần tử từ set1 và set2 (union), lấy ra không lặp lại khi trong 2 set đều có giá trị đó, 2 cách, cách này với cách trên

set7 = set1.union(set2)
print(set7)
print(set1 | set2 | set6)

# lấy tất cả nhưng trừ đi phần chung của 2 set
set8 = set1.symmetric_difference(set2)
print(set8)
print(set1 ^ set2)


# sum, len, min, max, join
