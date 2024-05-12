diem_cao = [78, 56, 67]
diem_moi = int(input("Nhập điểm mới của người chơi: "))
diem_cao.append(diem_moi)
diem_cao.sort(reverse=True)
print("Điểm mới đã được thêm vào danh sách điểm cao.")
print("Danh sách điểm cao mới (sắp xếp từ cao đến thấp):")
for diem in diem_cao:
    print(diem)
