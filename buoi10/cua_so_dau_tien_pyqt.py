import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class CuaSoDauTien(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cua so PyQt dau tien")
        self.resize(300, 200)
        layout = QVBoxLayout()
        nhan = QLabel("Xin chao PyQt!")
        layout.addWidget(nhan)
        self.setLayout(layout)


app = QApplication(sys.argv)
cua_so = CuaSoDauTien()
cua_so.show()
sys.exit(app.exec_())

# So sanh voi Tkinter:
# - Tkinter: cua_so = tk.Tk() ... cua_so.mainloop()
# - PyQt: QApplication quan ly toan bo ung dung; app.exec_() khoi dong vong lap
#   su kien (event loop) giong mainloop(): cho su kien (click, go phim...),
#   phan phoi den widget/slot, den khi dong cua so thi tra ve ma thoat cho sys.exit().
# - QApplication phai tao TRUOC moi widget; cua so phai goi show() moi hien.
