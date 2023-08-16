# + sum, len, max, min, join
lst = [1, 2, 3, 4]
total = sum(lst)
print(total)
# lấy total + thêm 10, khi không truyền vào sau dấu phẩy thì mặc định là 0
total = sum(lst, 10)
print(total)

# sum với một list khác
lst1 = [[1, 2, 3, 4], [10, 20, -10]]
total = sum(lst1, [0])
print(total)

# min
lst = ['a', 'b', 'c', 'd', 'f']
print(len(lst))
print(min(lst))

# join: có thể dùng cả "" và '', list ban đầu phải là list chuỗi, nếu ban đầu mà là list số thì ban đầu là số nguyên, mình
# phải convert về chuỗi bằng hàm map()
# hoặc lst = ['4','2','3','1'] thì mình ko cần map nữa bởi vì list này thành list chuỗi rồi
lst = [4, 2, 3, 1]
# sử dụng hàm map để convert từ 1 cái list số thành 1 cái list chuỗi
s = ' - '.join(map(str, lst))
print(s)
