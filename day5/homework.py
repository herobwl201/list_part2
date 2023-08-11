# 1. Cho danh sách (list) friends = ["Jen", "Jack", "Kenny", "Jelly", "Bob", "Henry", "Anne"]
friends = ["Jen", "Jack", "Kenny", "Jelly", "Bob", "Henry", "Anne"]
# Yêu cầu
# a. Lấy ra 4 người bạn đầu tiên trong list friends.
new_lst = friends[0:4:1]  # giá trị thứ 3 là step (bước nhảy)
# so sánh nó có khác với list ban đầu không (result: false)
print(new_lst is friends)
print(new_lst)
print(friends[0], friends[1], friends[2], friends[3])
# b. Lấy ra 4 người bạn cuối cùng trong list friends.
new_lst1 = friends[-1:-5:-1]  # giá trị thứ 3 là step (bước nhảy)
# so sánh nó có khác với list ban đầu không (result: false)
print(new_lst1 is friends)
print(new_lst1)
# c. Đảo ngược danh sách list friends.
new_lst2 = friends[::-1]
print(new_lst2)
# d. Lấy ra những người bạn từ vị trí thứ 1 đến hết.
new_lst3 = friends[1:]
print(new_lst3)
# e. Copy danh sách ban đầu thành một danh sách mới.
new_lst4 = friends[0:]  # lấy từ 1 đến hết
print(id(new_lst4))
print(new_lst4)
# f. Lấy ra những người bạn từ vị trí 2 đến sát cuối.
new_lst5 = friends[2:-1]
print(new_lst5)
print('__________________________________\n')
# 2. Cho danh sách các sinh viên chứa thông tin của mỗi sinh viên [id, tên, tuổi] như sau:
students=[["SV001", "Bob", 23], ["SV002", "Kenny", 34], ["SV003", "Henry", 45]]
print(students)
print(type(students))
print(id(students))
# Yêu cầu
# a. Lấy ra thông tin của sinh viên thứ nhất 
# và in ra định dạng "ID: {id}, name: {name}, 
# age: {age}".
print(students[0])
# b. Lấy ra tuổi của sinh viên thứ hai.
print(students[1][2])
# c. Lấy ra thông tin của hai sinh viên cuối cùng.
print(students[-1],students[-2])
# d. Lấy ra id của sinh viên thứ ba.
print(students[2][0])