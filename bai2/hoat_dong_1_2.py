print("=== Bai tap 1.1: input() va ep kieu ===")

ho_ten = input("Nhap ho ten: ")
nam_sinh = int(input("Nhap nam sinh: "))
diem_tb = float(input("Nhap diem trung binh: "))

print("Python", "la", "ngon", "ngu", "lap trinh", sep="-")
print("Dong 1", end=" | ")
print("Dong 2")

print("\nThu nghiem sep voi ', ':")
print("Python", "la", "ngon", "ngu", "lap trinh", sep=", ")

print("\nThu nghiem sep voi '\\n':")
print("Python", "la", "ngon", "ngu", "lap trinh", sep="\n")

print("\n=== Bai tap 1.3: So sanh 3 cach dinh dang chuoi ===")
print(f"Ho ten: {ho_ten} - Nam sinh: {nam_sinh} - DTB: {diem_tb:.2f}")
print("Ho ten: {} - Nam sinh: {} - DTB: {:.2f}".format(ho_ten, nam_sinh, diem_tb))
print("Ho ten: %s - Nam sinh: %d - DTB: %.2f" % (ho_ten, nam_sinh, diem_tb))

print("\n=== Bai tap 2.1: Chu thich ===")
# Chu thich mot dong: khai bao thong tin sinh vien
"""
Chu thich/docstring nhieu dong:
Chuong trinh quan ly diem sinh vien - Buoi 2
"""
ho_ten_2_1 = "Tran Thi B"
print(f"Khoi tao ho ten trong BT 2.1 thanh cong: {ho_ten_2_1}")

print("\n=== Bai tap 2.2: Cac kieu trich dan & escape ===")
s1 = 'Xin chao'
s2 = "Ban co khoe khong?"
s3 = '''Day la
mot chuoi
nhieu dong'''
s4 = "Duong dan: C:\\Python\\data"
s5 = r"Duong dan raw: C:\Python\data"
s6 = "Toi ten la \"Nam\", con ban ten gi?"

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)
