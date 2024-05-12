numbers = []
while True:
    num = float(input("Nhập một số (nhập 0 để kết thúc): "))
    if num == 0:
        break
    numbers.append(num)
total = sum(numbers)
if len(numbers) > 0:
    average = total / len(numbers)
    print("Trung bình của các số là:", average)
else:
    print("Danh sách rỗng, không có số nào để tính trung bình.")
