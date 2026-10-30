"""Hoat dong 3: Matplotlib - bieu do cot & bieu do duong."""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# Tim file CSV canh file .py -> chay duoc tu bat ky thu muc nao
THU_MUC = Path(__file__).resolve().parent
DUONG_DAN_CSV = THU_MUC / "diem_sinh_vien.csv"

# Cau hinh font mac dinh cua matplotlib ho tro tieng Viet (DejaVu Sans)
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.titlesize": 12,
    "axes.titleweight": "bold",
})

df = pd.read_csv(DUONG_DAN_CSV)
diem_trung_binh_mon = df.groupby("mon_hoc")["diem"].mean().round(2)

# --- 3.1 Bieu do cot: diem trung binh theo mon hoc ---
plt.figure(figsize=(6, 4))
cot = plt.bar(diem_trung_binh_mon.index, diem_trung_binh_mon.values,
              color="skyblue", edgecolor="steelblue", width=0.55)
plt.bar_label(cot, fmt="%.2f", padding=2, fontweight="bold")
plt.title("Điểm trung bình theo môn học")
plt.xlabel("Môn học")
plt.ylabel("Điểm trung bình")
plt.ylim(0, 10)
plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig(THU_MUC / "bieu_do_cot.png", dpi=150)
plt.show()

# --- 3.2 Bieu do duong: xu huong diem qua cac lan kiem tra ---
lan_kiem_tra = [1, 2, 3]
diem_qua_cac_lan = [6.5, 7.5, 8.5]

plt.figure(figsize=(6, 4))
plt.plot(lan_kiem_tra, diem_qua_cac_lan, marker="o", color="green",
         linewidth=2, markersize=8, label="Điểm thực tế")
for x, y in zip(lan_kiem_tra, diem_qua_cac_lan):
    plt.annotate(f"{y}", (x, y), textcoords="offset points",
                 xytext=(0, 9), ha="center", fontweight="bold")
plt.xticks(lan_kiem_tra, [f"Lần {i}" for i in lan_kiem_tra])
plt.title("Xu hướng điểm qua các lần kiểm tra")
plt.xlabel("Lần kiểm tra")
plt.ylabel("Điểm số")
plt.ylim(0, 10)
plt.grid(linestyle="--", alpha=0.4)
plt.legend()
plt.tight_layout()
plt.savefig(THU_MUC / "bieu_do_duong.png", dpi=150)
plt.show()

print("Da luu 2 bieu do: bieu_do_cot.png, bieu_do_duong.png")
