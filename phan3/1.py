numbers = [17, 5, 23, 9, 14]
search_number = int(input("Nhập vào một số bạn muốn kiểm tra: "))
if search_number in numbers:
    position = numbers.index(search_number) + 1
    print(f"Số {search_number} có trong list và đứng ở vị trí thứ {position}.")
else:
    print("Số này không có trong list.")
