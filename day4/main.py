# 1. Tạo một movies list chứa tên các bộ phim đã xem.
movies_list = ["Iron man", "Spiderman",
               "Batman", "Superman", "Antman", "Aquaman"]
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
