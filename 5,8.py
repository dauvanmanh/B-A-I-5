import search

# Nhập danh sách từ bàn phím
dlist = list(map(int, input("Nhập các phần tử của danh sách, phân tách bởi dấu cách: ").split()))
item = int(input("Nhập phần tử cần tìm: "))

# Tìm kiếm phần tử
found, index = search.Sequential_Search(dlist, item)

if found:
    print("Phần tử", item, "được tìm thấy tại chỉ mục", index)
else:
    print("Phần tử", item, "không được tìm thấy")
