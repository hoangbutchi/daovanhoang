import math

print("=== Bai tap 3.1: Cac kieu so & chuyen doi ===")
so_nguyen = 15
so_thuc = 4.2
so_phuc = 3 + 4j
print("Kieu du lieu:", type(so_nguyen), type(so_thuc), type(so_phuc))
print("Ep int -> float:", float(so_nguyen))
print("Ep float -> int (cat phan thap phan):", int(so_thuc))

print("\n=== Bai tap 3.2: Ham built-in xu ly so ===")
a = -7
b = 2.6789
c, d = 17, 5

print("Gia tri tuyet doi abs(a):", abs(a))
print("Lam tron round(b):", round(b))
print("Lam tron round(b, 2):", round(b, 2))
print("pow(c, 2):", pow(c, 2))
print("divmod(c, d):", divmod(c, d))

print("\nSo sanh pow(c, 2) va c ** 2:")
print(f"pow(17, 2) = {pow(c, 2)}")
print(f"17 ** 2 = {c ** 2}")

print("\n=== Bai tap 3.3: Phuong trinh bac hai (2 nghiem phan biet) ===")
a_pt, b_pt, c_pt = 1, -3, 2
delta = b_pt ** 2 - 4 * a_pt * c_pt
x1 = (-b_pt + math.sqrt(delta)) / (2 * a_pt)
x2 = (-b_pt - math.sqrt(delta)) / (2 * a_pt)
print(f"Delta = {delta}")
print(f"Nghiem x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")


print("\n=== Bai tap 4.1: Indexing & slicing ===")
cau = "Lap trinh Python rat thu vi"
print("Ky tu dau tien [0]:", cau[0])
print("Ky tu cuoi cung [-1]:", cau[-1])
print("Cat tu vi tri 4 den truoc 10 [4:10]:", cau[4:10])
print("Tu dau den vi tri 8 [:8]:", cau[:8])
print("Tu vi tri 11 den het [11:]:", cau[11:])
print("Dao nguoc chuoi [::-1]:", cau[::-1])

is_palindrome = cau == cau[::-1]
print(f"Chuoi '{cau}' co phai la palindrome khong? {is_palindrome}")

print("\n=== Bai tap 4.2: Tinh bat bien (immutable) ===")
ten = "Nam"
print(f"Chuoi ban dau: {ten}")
ten_moi = "T" + ten[1:]
print(f"Chuoi sau khi thay the thong qua ghep chuoi: {ten_moi}")

print("\n=== Bai tap 4.3: Cac phuong thuc xu ly chuoi ===")
cau_4_3 = " Toi dang HOC Python rat vui "
print("strip():", f"'{cau_4_3.strip()}'")
print("strip().upper():", cau_4_3.strip().upper())
print("strip().lower():", cau_4_3.strip().lower())
print("strip().replace():", cau_4_3.strip().replace("HOC", "hoc"))
print("strip().split():", cau_4_3.strip().split())
print("len(strip().split()):", len(cau_4_3.strip().split()))
print("count('o'):", cau_4_3.count("o"))
print("find('Python'):", cau_4_3.find("Python"))
print("strip().startswith('Toi'):", cau_4_3.strip().startswith("Toi"))
print("strip().endswith('vui'):", cau_4_3.strip().endswith("vui"))
print("join():", "-".join(["Python", "that", "thu", "vi"]))

print("\n=== Bai tap 4.4: Chuan hoa ho ten ===")
ho_ten_tho = " nguyen van an "
ho_ten_sach = " ".join(ho_ten_tho.split()).title()
print(f"Ho ten tho: '{ho_ten_tho}'")
print(f"Ho ten sach: '{ho_ten_sach}'")
