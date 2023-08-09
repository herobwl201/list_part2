# 1. Tạo một movies list chứa tên các bộ phim đã xem.
movies_list = ["Iron man", "Spiderman",
               "Batman", "Superman", "Antman", "Aquaman"]
print(movies_list, type(movies_list))
# 2. Sử dụng hàm input để nhập vào một bộ phim khác không có trong movies list.
movies_list.insert(0, "Yusha")
print(movies_list)
# 3. Thêm bộ phim vừa nhập vào cuối danh sách movies.
movies_list.append("Yusha")
print(movies_list)
# 4. In ra bộ phim đầu tiên, cuối cùng và ở giữa movies list.
print(movies_list[0], movies_list[7], movies_list[4])
# 5. Tính tống bộ phim có trong movies list.
amount = len(movies_list)
print(amount)
# 6. Xóa bộ phim đầu và cuối trong movies list.
del movies_list[0]
del movies_list[6]
print(movies_list)
# 7. Lấy ra và xóa bộ phim cuối cùng trong movies list.
print(movies_list[5])
del movies_list[5]
print(movies_list)
# 8. Chèn một bộ phim bất kỳ vào đầu danh sách movies.
movies_list.insert(0, "Fairy Heart")
print(movies_list)
# 9. Đếm số bộ phim có tiêu đề là "One Piece".
search_query = "One Piece"
one_piece_count = 0

for movie in movies_list:
    if search_query.lower() in movie.lower():
        one_piece_count += 1

print(f"Số bộ phim có tiêu đề 'One Piece': {one_piece_count}")
# 10. Tìm vị trí của bộ phim có tên là "gió".
search_query = "gió"
positions = []

for index, movie in enumerate(movies_list):
    if search_query.lower() in movie.lower():
        positions.append(index)

print(f"Vị trí của bộ phim có tên 'gió': {positions}")
# 11. Thêm một danh sách bộ phim khác vào cuối danh sách movies ban đầu.
movies_list.extend(["Into you", "Love kill p", "Hello world"])
print(movies_list)
# 12. Xóa tất cả các bộ phim có trong danh sách
movies_list.clear()
print(movies_list)
