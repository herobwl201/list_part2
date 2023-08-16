# + Dictionary: chứa key: value
import json
student = {
    "name": "Bob",
    "age": 23,
    "grades": [45, 67, 90, 98,99]
}

print(json.dumps(student, indent=4))

# Lấy giá trị trong dictionary
# Cách 1:
value = student["name"]
print(value) # Result: Bob
# Cách 2
value1 = student.get("id","SV001") #Truyền giá trị vào dictionary
print(value1)
print(student)

# Thêm giá trị vào dictionary 
student["id"] = "SV001" # thêm vào cuối danh sách dictionary <=> hàm append trong cái list
print(student)

# update giá trị trong dictionary
student["name"] = "Jack"
print(student) # Bob -> Jack

# cách update nhiều giá trị đc nối vào cuối list
student.update(id="SV001", gender="male")
print(json.dumps(student, indent=4))

info = {
    'id': "SV001",
    'gender': "male"
}
student.update(info)
print(json.dumps(student, indent=4)) # kết quả tương tự dòng 30

# có thể sử dụng list tuple
info1 = [
    ('id', "SV001"),
    ('gender', 'male')
]
print(json.dumps(student, indent=4)) # kết quả tương tự dòng 30
print('---------------------------------------------------')
# remove

students = {
    "name": "Bob",
    "age": 23,
    "grades": [45, 67, 90, 98,99]
}
# Cách xóa 1
value = students.pop('name')
print(value)
print(json.dumps(students, indent=4))

# Cách xóa 2: xóa lun khỏi dictionary và bộ nhớ
del students["age"]
print(json.dumps(students, indent=4))

# Lấy ra phần tử cuối cùng trong dictionary
tup = students.popitem() # Xóa đi cái cuối và trả về cái cưới đó
print(tup)
print(json.dumps(students, indent=4)) #đã xóa grades

# keys
keys = list(student) # lấy ra những key trong list
print(keys)

values = list(student.values()) # Lấy ra tất cả giá trị trong dictionary, của từng cái key mà nó chứa
print(values)

items = list(student.items()) # lấy cả keys lẫn value
print(items)

# clear all
student.clear()
print(student)