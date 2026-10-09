"""Hoat dong 1 + 2: Cua so Tkinter dau tien + Frame to chuc giao dien."""
import tkinter as tk


def main():
    cua_so = tk.Tk()
    cua_so.title("Ung dung demo")
    cua_so.geometry("400x300")
    cua_so.resizable(False, False)  # khong cho keo rong/cao
    # Thu doi thanh resizable(True, False) -> chi keo duoc chieu rong, khong keo duoc chieu cao
    # resizable(True, True) -> keo tu do ca 2 chieu

    # --- Hoat dong 1: Label chao ---
    # --- Hoat dong 2: dung Frame de chia vung giao dien ---
    khung_tren = tk.Frame(cua_so, bg="lightblue", height=100)
    khung_tren.pack(fill="x")

    khung_duoi = tk.Frame(cua_so, bg="lightyellow")
    khung_duoi.pack(fill="both", expand=True)

    tk.Label(khung_tren, text="Xin chao Tkinter!", font=("Arial", 16),
             bg="lightblue").pack(pady=10)
    tk.Label(khung_tren, text="Khu vuc tieu de", bg="lightblue").pack()

    tk.Label(khung_duoi, text="Khu vuc noi dung", bg="lightyellow").pack(pady=10)

    cua_so.mainloop()


if __name__ == "__main__":
    main()

# Ghi chu: Vai tro cua Frame:
# - Frame la khung chua de nhom cac widget lien quan lai voi nhau.
# - Nen nhom vao Frame thay vi dat het len cua so chinh vi:
#   + De quan ly bo cuc rieng cho tung khu vuc (tieu de / noi dung / nut bam...).
#   + De bao tri, an/hien ca nhom chi voi 1 lenh, tai su dung code.
