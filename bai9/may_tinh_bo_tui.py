
import tkinter as tk
from tkinter import messagebox

cua_so = tk.Tk()
cua_so.title("May tinh bo tui")
cua_so.geometry("400x400")
cua_so.resizable(False, False)

bien_bieu_thuc = tk.StringVar()

hien_thi = tk.Entry(cua_so, textvariable=bien_bieu_thuc,
                    font=("Arial", 20), justify="right")
hien_thi.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")


def bam_phim(phim):
    bien_bieu_thuc.set(bien_bieu_thuc.get() + phim)


def xoa_trang():
    bien_bieu_thuc.set("")


def tinh_ket_qua():
    try:
        ket_qua = eval(bien_bieu_thuc.get(), {"__builtins__": None}, {})
        bien_bieu_thuc.set(str(ket_qua))
    except Exception as e:
        messagebox.showerror("Loi", f"Bieu thuc khong hop le: {e}")
        bien_bieu_thuc.set("")



nut_bam = [
    ("7", "7"), ("8", "8"), ("9", "9"), ("/", "/"),
    ("4", "4"), ("5", "5"), ("6", "6"), ("*", "*"),
    ("1", "1"), ("2", "2"), ("3", "3"), ("-", "-"),
    ("0", "0"), (".", "."), ("=", "="), ("+", "+"),
]

for i, (chu, phim) in enumerate(nut_bam):
    dong = 1 + i // 4
    cot = i % 4
    if phim == "=":
        tk.Button(cua_so, text=chu, width=5, height=2, font=("Arial", 14),
                  command=tinh_ket_qua).grid(row=dong, column=cot, padx=5, pady=5)
    else:
        tk.Button(cua_so, text=chu, width=5, height=2, font=("Arial", 14),
                  command=lambda p=phim: bam_phim(p)).grid(row=dong, column=cot, padx=5, pady=5)

tk.Button(cua_so, text="C", width=22, height=2, font=("Arial", 14),
          bg="orange", command=xoa_trang).grid(row=5, column=0, columnspan=4, padx=5, pady=5)

cua_so.mainloop()
