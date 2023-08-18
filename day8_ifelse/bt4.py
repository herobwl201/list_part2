# Giải và biện luận phương trình bậc nhất một ẩn ax + b = 0 (ẩn x, a và b là hai số cho trước)
a, b = (map(eval, input("nhập a và b: ").split()))
print(f"Biểu thức phương trình bậc nhất: {a}x + {b} = 0")
if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    print(f"Nghiệm của phương trình là: x = {-b/a}")
