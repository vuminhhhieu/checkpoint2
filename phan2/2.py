colors = ["blue", "red", "teal", "green"]
print("Danh sách màu:")
for i, color in enumerate(colors, start=1):
    print(f"{i}. {color}")
choice = input("Bạn muốn xoá màu theo vị trí hay giá trị? (vị trí/Giá trị): ")
if choice.lower() == "vị trí":
    index = int(input("Nhập số thứ tự của màu bạn muốn xoá (tính từ 1): "))
    if 1 <= index <= len(colors):
        del colors[index - 1]
        print("Danh sách màu sau khi xoá:")
        print(colors)
    else:
        print("Vị trí không hợp lệ!")
elif choice.lower() == "giá trị":
    color_to_delete = input("Nhập màu bạn muốn xoá: ")
    if color_to_delete in colors:
        colors.remove(color_to_delete)
        print("Danh sách màu sau khi xoá:")
        print(colors)
    else:
        print("Màu không tồn tại trong danh sách!")
else:
    print("Lựa chọn không hợp lệ!")
