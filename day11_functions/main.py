'''
Python funtions: Hàm là khối lệnh chỉ chạy khi nó được gọi
'''

# vd1:

def my_func():
    print("Hello")


my_func() # Gọi để chạy hàm

# vd2:

def my_func(msg):
    print(msg)


my_func("Hello") # Gọi để chạy hàm

# Có thể cho nhiều tham số

def show_full_name(fname, lname): # Tên hàm thường là động từ để nó ám chỉ một cái chức năng
    print(f"{fname} {lname}")

show_full_name("John", "Doe")


# Có thể cho nhiều tham số 2

def get_full_name(fname, lname = "Doe"): # Tên hàm thường là động từ để nó ám chỉ một cái chức năng
    return f"{fname} {lname}"

full_name = get_full_name("John")
print(full_name)

# Có thể cho nhiều tham số 3

def get_full_name(fname, lname = "Doe"): # Tên hàm thường là động từ để nó ám chỉ một cái chức năng
    if fname:
        return f"{fname} {lname}"
    
    return f"Kenny {lname}"

full_name = get_full_name("") # Bool rỗng nghĩa là dòng này false, nó sẽ chạy dòng return
print(full_name)


print("--------------------")

def add(x, y = 40):
    return x + y

print(add(x = 10, y = 100))

print("--------------------")

def func(lst = []): # tránh kiểu list và dictionary truyền vào hàm bởi vì chúng có những tham số có thể thay thế đc. vậy nên tốt nhất là dùng tuple.
    lst.append(2)
    print(lst)

func() # [2]
func() # [2, 2]

print("--------------------")

friends = ["Kenny", "Bob", " Jen"]

def my_func():
    # friends = friends + ["Joe"] # error: friends 2 đc tham chiếu trc khi gọi hàm, cách sửa: thay friends 1 thành f, do friends 1 ko cho thấy cái list đang cần liên kết và friends 1 đang chặn friends 2 tham chiếu dữ liệu.
    f = friends + ["Joe"]
    print(f)

my_func()

print("--------------------")

# Hàm không có tên: lambda function

add = lambda x, y: x + y
print(add(1, 2))

# First class function: là một hàm mà nó nhận một cái hàm khác

def greet(msg):
    print("Hello" + msg)
    # (return None)

hello = greet
print(hello("Jen"))

print("--------------------")

def func():
    pass # pass để không bị lỗi khi để trống hàm func()

print("--------------------")

# *args
def add(*args): # *args * dùng để tập hợp, trở thành 1 tuple để colect các số 1, 2, 3, 4
    print(type(args))
    return sum(args)

print(add(1, 2, 3, 4))

print("--------------------")

# *args
lst = [4, 3, 2, 1]
print(*lst)

print("--------------------")

# *args
lst = [3, 10, 4, 5, 6, 7]
first, *mid, last = lst

print(first)
print(mid)
print(last)

# *args
def add(*lst, operation): # đối số operation chưa đc định nghĩa
    return operation(lst)

print(add(1, 2, 3, 4, operation=sum))

# *args
def my_func():
    print("Hello")

my_func()

print("--------------------")


lst = [[]] * 5

lst[1].append(2)
print(lst)