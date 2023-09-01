lst = [4, 100, 5 , 6]

# in ra các giá trị trong list, áp dụng cho cả set và tuple
for value in lst:
    print(value)

d = {  # dictionary
    'a': 1,
    'b': 2,
    'c': 3
}
print(type(d))

for key in d: 
    print(key) # print ra key 'a', 'b', 'c'

for value in d.values():
    print(value) # print ra value '1', '2', '3'

for item in d.items():
    print(item) # print ra cả key và value

'''
+ Iterable: list, tuple, set, dict
'''

# List comprehensions: hoàn thiện list

lst = [1,2,3,4]

# wishes: new_lst = [2,4,6,8]

# Cách 1:
""" new_lst = []

for x in lst:
    val = x * 2
    new_lst.append(val)

print(new_lst) """

# Cách 2:
new_lst = [val * 2 for val in lst] # cú pháp của list comprehensions
print(new_lst)

# Set comprehension
set_a = {"a", "c", "b",}

new_set = {s.upper() for s in set_a}
print(new_set)

# Dict comprehension
d = {
    'a': 1,
    'b': 2,
    'c': 3
}
new_d = {
    k: v * 2
    for k, v in d.items()
}
print(new_d)

