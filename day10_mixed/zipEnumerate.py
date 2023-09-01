'''
+ zip: ghép các giá trị cùng vị trí của 2 list lại với nhau để tạo thành 1 cái
+ enumerate: trả về 1 dãy các tuple bao gồm giá trị của một thành phần trong list và vị trí của nó trong list
'''
# zip
lst1 = ['a', 'b', 'c']
lst2 = (1, 2, 3, 4)

print(list(zip(lst1, lst2)))

# enumerate
lst = ["a", "b", "c"]

print(list(enumerate(lst))) # [(0, 'a'), (1, 'b'), (2, 'c')]

print(list(enumerate(lst, start=1))) # [(1, 'a'), (2, 'b'), (3, 'c')]
print("----------------------")

# ----------------------------
lst1 = ['a', 'b', 'c']
lst2 = (1, 2, 3, 4)
print(list(zip(lst1,lst2))) # convert về list: ra đc list tuple
print(dict(zip(lst1, lst2))) # convert về dict: ra đc dict

# ví dụ csv
student = {
    'name': 'Bog',
    'age': 23,
    'gender': 'male'
}

