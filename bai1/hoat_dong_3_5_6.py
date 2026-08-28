# hoạt động 3
ten = "Nguyen Van A"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2
MUC_LUONG_TOI_THIEU = 5000000

print("Tên:", ten)
print("Điểm toán:", diem_toan)
print("Điểm văn:", diem_van)
print("Số lượng môn học:", so_luong_mon_hoc)
print("Mức lương tối thiểu:", MUC_LUONG_TOI_THIEU)
# hoạt động 5
# 5.1
a = 17
b = 5
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)
# 5.2
diem = 6.5
tuoi = 20
la_diem_kha = (diem >= 6.5) and (diem < 8.0)
print("diem đạt loại Khá?", la_diem_kha)

ngoai_do_tuoi_lao_dong = (tuoi < 18) or (tuoi > 60)
print("tuoi chưa đủ 18 hoặc trên 60?", ngoai_do_tuoi_lao_dong)
print("Phủ định điều kiện tuổi:", not ngoai_do_tuoi_lao_dong)
# 5.3
x = 10
x += 5
print("x =", x)
x -= 3
print("x =", x)
x *= 2
print("x =", x)
x /= 4
print("x =", x)
x //= 2
print("x =", x)
x **= 3
print("x =", x)

danh_sach = [1, 2, 3, "python"]
co_trong_list = 3 in danh_sach
print("3 có nằm trong danh_sach?", co_trong_list)

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]
print("list1 is list2?", list1 is list2)
print("list1 is list3?", list1 is list3)
# 5.4
print("2 + 3 * 4 ** 2 =", 2 + 3 * 4 ** 2)
print("(2 + 3) * 4 ** 2 =", (2 + 3) * 4 ** 2)
print("10 > 5 and 3 < 1 or not False =", 10 > 5 and 3 < 1 or not False)
# hoạt động 6
# 6.1
bien = 10
print(bien, type(bien))

bien = "Xin chao"
print(bien, type(bien))

bien = 3.14
print(bien, type(bien))

bien = True
print(bien, type(bien))
# 6.2
ho_ten = "Nguyen Van A"
diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0

dtb = (diem_toan + diem_ly + diem_hoa) / 3

la_gioi = dtb >= 8.0
la_kha = dtb >= 6.5 and dtb < 8.0
la_trung_binh = dtb >= 5.0 and dtb < 6.5
la_yeu = dtb < 5.0

print(ho_ten, "- DTB:", round(dtb, 2))
print("Dat loai Gioi?", la_gioi)
print("Dat loai Kha?", la_kha)
print("Dat loai Trung binh?", la_trung_binh)
print("Dat loai Yeu?", la_yeu)
print("Kieu du lieu cua la_gioi:", type(la_gioi))
