# Nhập vào một danh sách những số nguyên và hiển thị gấp đôi của các số trong danh sách sử dụng list

lst = list(map(int, input("Nhập vào các số nguyên: ").split()))
new_lst = [ n * 2 for n in lst]
print(new_lst)