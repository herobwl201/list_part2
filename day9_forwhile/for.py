# vòng lặp for: lặp với số lần xác định

# print 5 dòng lệnh hello world, vòng lặp chạy từ 0 -> 5 thì dừng lại
for _ in range(5): # _ : là một tên biến, biến này không được dùng trong vòng lặp
    print("Hello world!")

# Tìm số chia hết cho 2 trong khoảng từ 1 -> 21
for i in range(1,21): 
    if i % 2 == 0:
        print(i, end = ' ')

