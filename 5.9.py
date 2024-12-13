import binary_search

# Nhập danh sách từ bàn phím
lst = list(map(int, input("Nhập các phần tử của danh sách, phân tách bởi dấu cách: ").split()))
value = int(input("Nhập phần tử cần tìm: "))

# Sắp xếp danh sách để áp dụng tìm kiếm nhị phân
lst.sort()

# Tìm kiếm phần tử
found = binary_search.binary_search(lst, value)

# In kết quả
if found:
    print("Phần tử", value, "được tìm thấy trong danh sách")
else:
    print("Phần tử", value, "không được tìm thấy trong danh sách")
