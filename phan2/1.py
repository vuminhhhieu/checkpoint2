colors = ["blue", "red", "teal", "green"]
print("Danh sách màu:")
for i, color in enumerate(colors, start=1):
    print(f"{i}. {color}")
index = int(input("Nhập số thứ tự của màu bạn muốn xem (tính từ 1): "))
if 1 <= index <= len(colors):
    selected_color = colors[index - 1]
    print(f"Màu ở vị trí {index} là: {selected_color}")
else:
    print("Vị trí không hợp lệ!")

