#
# 1. Cho một list chứa các tuple như sau: friends =[("Bob", "Male"), ("Anna", "Female"), ("Max", "Male")]
# a. Cho biết chiều dài của friends.
# b. Lấy ra phần tử đầu, cuối và giữa và kiểm tra kiểu của chúng.
# c. Nhập vào tên (name) và giới tính (gender) của một người bạn và sau đó
# append vào friends tuple gồm hai giá trị (name, gender)


# a.
friends = [("Bob", "Male"), ("Anna", "Female"), ("Max", "Male")]
print(friends)
lenlist = len(friends)
print(lenlist)

# b.
phantudau = friends[0]
print(phantudau)
print(type(phantudau))

phantugiua = friends[1]
print(phantugiua)
print(type(phantugiua))

phantucuoi = friends[2]
print(phantucuoi)
print(type(phantucuoi))

# c.
name = input('Nhập tên: ')
gender = input('gender: ')
addfriend = (name, gender)
friends.append(addfriend)
print(friends)


'''
2. Tạo một set trống có tên là set_a
a. Thêm 'Anna' vào set_a
b. Thêm một tuple ('Kenny', 'Jen', 'Danny')
c. In ra set_a và tính chiều dài của nó.
d. Zóa 'Jen' ra khỏi set_A
e. Xóa tất cả giá trị từ set_a.
'''

# Tạo set rỗng
set_a = set()

# a.
set_a.add('Anna')
print(set_a)

# b.
tup = ('Kenny', 'Jen', 'Danny')
set_a.update(tup)
print(set_a)

# c.
print(set_a)
length = len(set_a)
print(length)

# d.
set_a.remove('Jen')
print(set_a)

# e.
set_a.clear()
print(set_a)
