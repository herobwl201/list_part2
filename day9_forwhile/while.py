# vòng lặp while: lặp với số lần ko xác định
s = input('> ')

while s != 'q': # result: lặp lại vô tận không dừng, "<" luôn luôn khác q
    print("hello")
    s = input('> ')

# lồng nhau
for i in range(5):
    for j in range(3):
        print(i, j, sep = " - ")