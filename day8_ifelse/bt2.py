# Nhập vào một năm bất kt2. Kiểm tra xem năm đó có phải năm nhuận hay không?
# Năm nhuận là năm chia hết cho 4 và không chia hết cho 100 hay chia hết cho 400
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input("Nhập vào một năm: "))
if is_leap_year(year):
    print(f"{year} là năm nhuận.")
else:
    print(f"{year} không phải là năm nhuận.")


# Cách 2:
year = int(input("Nhập vào năm: "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"Năm {year} là năm nhuận")
else:
    print(f"Năm {year} không phải là năm nhuận.")