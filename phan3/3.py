numbers = []
while True:
    number = int(input("Nhập một số nguyên (nhập 0 để kết thúc): "))
    if number == 0:
        break  
    numbers.append(number)
total = sum(numbers)
print("Tổng của dãy số là:", total)
