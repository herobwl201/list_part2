""" 
+ break: thoát hoàn toàn ra khỏi vòng lặp chứa nó
+ continue: bỏ qua các câu lệnh bên dưới nó và chuyển sang mộ lần lặp mới
"""

""" for i in range(1,21):
    if i > 5:
        break # khi mà i > 5 nó sẽ break (thoát ra) khỏi vòng lặp n.
    print(i, end = ' ') """

for i in range(1,21):
    if i % 2 == 0:
        continue # i sẽ in ra những số lẻ thay vì số chia hết cho 2 như ở chỗ đkiện if, phần số chia hết cho 2 được lưu vào continue và đc bỏ qua.
    print(i, end = ' ')