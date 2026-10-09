"""Hoat dong 4.3: Dung bind() de bat su kien ban phim / chuot."""
import tkinter as tk


def khi_go_phim(event):
    nhan_thong_bao.config(text=f"Ban vua nhan phim: {event.char}")


def khi_click_chuot(event):
    nhan_thong_bao.config(text=f"Ban vua click tai toa do: ({event.x}, {event.y})")


cua_so = tk.Tk()
cua_so.title("Vi du bind()")
cua_so.geometry("400x250")

nhan_thong_bao = tk.Label(cua_so, text="Hay go phim hoac click chuot",
                          font=("Arial", 12))
nhan_thong_bao.pack(pady=30)

cua_so.bind("<Key>", khi_go_phim)
cua_so.bind("<Button-1>", khi_click_chuot)

cua_so.mainloop()

# Ghi chu:
# - command: chi dung cho mot so widget (chu yeu la Button),
#   tu dong goi ham khi bam nut, khong nhan doi tuong event.
# - bind(): dung duoc cho nhieu loai su kien (phim, chuot, focus...)
#   va nhieu widget (ke ca cua so chinh), ham xu ly nhan tham so event
#   chua thong tin chi tiet (phim nao, toa do click...).
