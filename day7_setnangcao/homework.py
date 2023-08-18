import json
# Bài tập

# 1. Cho hai tập hợp (set)
art_students = {"John", "Max", "Anna", "Bob", "Obito"}
math_students = {"Max", "Mery", "David", "Anna", "Naruto", "John"}

# Tìm những người bạn học cả vẽ lẫn toán
set = art_students.intersection(math_students)
print(set)
# Tìm những người bạn học vẽ nhưng không học toán
set = art_students.difference(math_students)
print(set)
# Tìm những người bạn học toán nhưng không học vẽ
set = math_students.difference(art_students)
print(set)
# Tìm những người bạn học vẽ hay toán không phải cả hai
set = art_students.symmetric_difference(math_students)
print(set)
print("Những người bạn học vẽ hay toán không phải cả hai", set)
# Tìm tất cả những người bạn
set = art_students.union(math_students)
print(set)

# 2. Cho dict sau:
album_info = {
    "album_name": " The Dark Side of the Moon",
    "band": "Pink Floyd",
    "release_year": 1973,
    "track list": [
        "Speak to me",
        "Breath",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    ]
}

# Yêu cầu:

# 1. Lấy ra giá trị của các key sau: album_name, release_year bằng hai cách

# Cách 1:
value = album_info["album_name"], album_info["release_year"]
print(value)

# Cách 2:
value = album_info.get("album_name"), album_info.get("release_year")
print(value)

# 2. Thay đổi giá trị của key: release_year từ 1973 thành 1971
album_info["release_year"] = "1971"
print(json.dumps(album_info, indent=4))

# 3. Xóa phần tử với key là track_list
del album_info["track list"]
print(json.dumps(album_info, indent=4))

# 4. Thêm một key mới là amount = 2000 bằng hai cách

# Cách 1:
album_info.update(amount=2000)
print(json.dumps(album_info, indent=4))

# Cách 2:
info = {
    'amount': 2000
}
print(json.dumps(album_info, indent=4))
# 5. Làm trống dict: album_info
album_info.clear()
print(album_info)
