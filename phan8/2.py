def hien_thi_5_diem_cao_nhat(diem_cao):
    print("Danh sách 5 điểm cao nhất:")
    for i in range(min(5, len(diem_cao))):
        print(diem_cao[i])
diem_cao = [78, 70, 67, 56, 45]
diem_moi = int(input("Nhập điểm mới của người chơi: "))
diem_cao.append(diem_moi)
diem_cao.sort(reverse=True)
hien_thi_5_diem_cao_nhat(diem_cao)
