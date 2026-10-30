"""Hoat dong 1: NumPy - mang & phep toan vector hoa."""
import numpy as np

# --- 1. List Python thuan vs mang NumPy (ndarray) ---
diem_list = [8.5, 7.0, 9.2, 6.5, 5.5]
diem_array = np.array(diem_list)

print("Kieu du lieu list :", type(diem_list))
print("Kieu du lieu array:", type(diem_array))
print("dtype cua array   :", diem_array.dtype)
print("So chieu (ndim)   :", diem_array.ndim, "| shape:", diem_array.shape)

# --- 2. Cong 0.5 vao TOAN BO mang: phep toan vector hoa ---
diem_cong_them = diem_array + 0.5
print("\nArray + 0.5 (vector hoa)   :", diem_cong_them)

# Cach lam tuong duong bang list thuan (Buoi 3): phai dung list comprehension
diem_cong_them_list = [diem + 0.5 for diem in diem_list]
print("List  + 0.5 (comprehension):", diem_cong_them_list)

# Chung minh list + 0.5 KHONG chay duoc (toan tu + tren list la noi list)
try:
    diem_list + 0.5
except TypeError as loi:
    print("list + 0.5 -> TypeError:", loi)

# --- 3. Thong ke mo ta ---
print("\n--- Thong ke diem ---")
print("Trung binh      :", np.mean(diem_array))
print("Lon nhat        :", np.max(diem_array))
print("Nho nhat        :", np.min(diem_array))
print("Do lech chuan   :", round(float(np.std(diem_array)), 2))
print("Trung vi        :", np.median(diem_array))
print("Phuong sai      :", round(float(np.var(diem_array)), 2))

# --- 4. Mang 2 chieu (ma tran) ---
ma_tran = np.array([[1, 2, 3], [4, 5, 6]])
print("\nMa tran:\n", ma_tran)
print("Kich thuoc (shape):", ma_tran.shape)
print("Ma tran nhan 2:\n", ma_tran * 2)

# --- 5. Vi du them: broadcasting & tinh theo truc ---
print("\nCong 1 vector [10, 20, 30] vao tung dong cua ma tran (broadcasting):\n",
      ma_tran + np.array([10, 20, 30]))
print("Tong theo cot (axis=0):", ma_tran.sum(axis=0))
print("Tong theo dong (axis=1):", ma_tran.sum(axis=1))
