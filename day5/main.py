# list in list
# copy list
# list slicing

# list in list
#              0           1             2
friends =[["Bob", 23],["Jen", 34],["Kenny", 56]] # list in list
print(type(friends))
print(type(friends[0]))
print(friends[0]) # Output: ['Bob',23]
print(friends[0][0]) # Output: Bob
print(friends[1][1]) # Output: 34
#print(friends[100][1]) # Output: IndexError: list index out of range

# copy list
lst1 = [1, 3, 2]
lst2 = lst1.copy() #vd: ra tiệm photo, photocopy 1 tờ giấy thành 1 bản, thì bản đó có cùng giá trị với bản gốc, nhưng
# về bản chất tờ giấy photo khác tờ giấy gốc nên khi so sánh bằng 'is' sẽ ra Output: False
# is - kiểm tra id bẳng nhau không?
print(id(lst1), id(lst2)) # in ra vị trí của cái list đó trong bộ nhớ
print(lst1 is lst2) # Output: False # is so sánh về mặt bộ nhớ
print(lst1 == lst2) # Output: True # == so sánh về mặt giá trị
print('-------------------------')
# list slicing - lấy ra một phần từ cái list ban đầu
# list slicing => new list. Nó trả về cho mình một cái danh sách mới hoàn toàn, tức là không phải cái danh sách ban đầu, nó nắm ở vị trí bộ
# nhớ khác danh sách ban đầu
# khác nhau giữa list slicing và reverse: reverse thực hiện ngay trên list ban đầu, list slicing là làm ra 1 cái list khác
#   0  1   2   3    4
#  -5 -4  -3   -2   -1
a= [1, 3 , 10, 100, 45]

# a[start:stop:step] - start không ghi mặc định là 0, stop là len, step là 1

new_lst = a[0:2:1] # giá trị thứ 3 là step (bước nhảy)
print(new_lst is a) # so sánh nó có khác với list ban đầu không (result: false)
print(new_lst)

new_lst1 = a[1:] # lấy từ 1 đến hết
print(new_lst1)

new_lst2 = a[1:-1] # lấy từ 1 đến hết
print(new_lst2)

new_lst3 = a[:] # lấy ra toàn bộ
print(new_lst3)

new_lst4 = a[::-1] # lật ngược lại cái list này
print(new_lst4) # 



