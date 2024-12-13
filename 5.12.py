import numpy as np

student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
student_height = np.array([40., 42., 45., 41., 38., 40., 42.])

# Sắp xếp sử dụng lexsort
sorted_index = np.lexsort((student_height, student_id))

print("Chỉ số:")
print(sorted_index)

print("Dữ liệu sắp xếp:")
for index in sorted_index:
    print(student_id[index], student_height[index])
