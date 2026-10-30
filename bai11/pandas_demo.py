"""Hoat dong 2: Pandas - doc CSV, thong ke, loc du lieu."""
from pathlib import Path

import pandas as pd

# Tim file CSV canh file .py -> chay duoc tu bat ky thu muc nao
THU_MUC = Path(__file__).resolve().parent
DUONG_DAN_CSV = THU_MUC / "diem_sinh_vien.csv"

# --- 2.1 Doc CSV & xem tong quan ---
df = pd.read_csv(DUONG_DAN_CSV)

print("=== 2.1 TONG QUAN DU LIEU ===")
print(df.head())                      # 5 dong dau
print("Shape (so dong, so cot):", df.shape)
print("Danh sach cot:", df.columns.tolist())
print("Kieu du lieu tung cot:")
print(df.dtypes)
print("Thong ke nhanh:")
print(df.describe().round(2))

# --- 2.2 Thong ke theo mon hoc ---
print("\n=== 2.2 THONG KE THEO MON HOC ===")
diem_trung_binh_mon = df.groupby("mon_hoc")["diem"].mean().round(2)
print(diem_trung_binh_mon)
print("Diem trung binh toan bo:", round(df["diem"].mean(), 2))
print("Diem cao nhat:", df["diem"].max())
print("Diem thap nhat:", df["diem"].min())

# --- 2.3 DTB tung sinh vien & loc dat / khong dat ---
print("\n=== 2.3 DIEM TRUNG BINH TUNG SINH VIEN ===")
diem_tb_sv = df.groupby("ho_ten")["diem"].mean().round(2)
print(diem_tb_sv)

sinh_vien_dat = diem_tb_sv[diem_tb_sv >= 5.0]
sinh_vien_khong_dat = diem_tb_sv[diem_tb_sv < 5.0]

print("\nSinh vien dat (DTB >= 5.0):")
print(sinh_vien_dat)
print("\nSinh vien khong dat (DTB < 5.0):")
print(sinh_vien_khong_dat)

# --- 2.4 Vi du them: sap xep va loc theo dong du lieu ---
print("\n=== 2.4 VI DU THEM ===")
print("Bang xep hang theo DTB giam dan:")
print(diem_tb_sv.sort_values(ascending=False))
print("\nCac dong co diem duoi 5.0:")
print(df[df["diem"] < 5.0])
