import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton, QGridLayout, QVBoxLayout, QMessageBox
)
from PyQt5.QtCore import Qt


class MayTinhBoTui(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("May tinh bo tui - PyQt")
        self.resize(300, 380)
        self.khoi_tao_giao_dien()

    def khoi_tao_giao_dien(self):
        self.man_hinh = QLineEdit()
        self.man_hinh.setReadOnly(True)
        self.man_hinh.setAlignment(Qt.AlignRight)
        self.man_hinh.setStyleSheet("font-size: 28px; padding: 8px;")

        cac_nut = [
            ["C", "<-", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "="],
        ]
        luoi = QGridLayout()
        for hang, danh_sach in enumerate(cac_nut):
            for cot, ky_tu in enumerate(danh_sach):
                nut = QPushButton(ky_tu)
                nut.setMinimumHeight(50)
                nut.setStyleSheet("font-size: 18px;")
                nut.clicked.connect(lambda _, k=ky_tu: self.xu_ly_nut(k))
                if ky_tu == "=":
                    luoi.addWidget(nut, hang, cot, 1, 2)
                else:
                    luoi.addWidget(nut, hang, cot)

        layout = QVBoxLayout()
        layout.addWidget(self.man_hinh)
        layout.addLayout(luoi)
        self.setLayout(layout)

    def xu_ly_nut(self, ky_tu):
        if ky_tu == "C":
            self.man_hinh.clear()
        elif ky_tu == "<-":
            self.man_hinh.setText(self.man_hinh.text()[:-1])
        elif ky_tu == "=":
            self.tinh_ket_qua()
        else:
            self.man_hinh.setText(self.man_hinh.text() + ky_tu)

    def tinh_ket_qua(self):
        bieu_thuc = self.man_hinh.text()
        if bieu_thuc == "":
            return
        try:
            if not all(c in "0123456789.+-*/% " for c in bieu_thuc):
                raise ValueError
            ket_qua = eval(bieu_thuc)
            if isinstance(ket_qua, float) and ket_qua.is_integer():
                ket_qua = int(ket_qua)
            self.man_hinh.setText(str(ket_qua))
        except ZeroDivisionError:
            QMessageBox.critical(self, "Loi", "Khong the chia cho 0.")
            self.man_hinh.clear()
        except Exception:
            QMessageBox.critical(self, "Loi", "Bieu thuc khong hop le.")
            self.man_hinh.clear()

    def keyPressEvent(self, event):
        phim = event.text()
        if phim and phim in "0123456789.+-*/%":
            self.xu_ly_nut(phim)
        elif event.key() in (Qt.Key_Return, Qt.Key_Enter):
            self.tinh_ket_qua()
        elif event.key() == Qt.Key_Backspace:
            self.xu_ly_nut("<-")
        elif event.key() == Qt.Key_Escape:
            self.xu_ly_nut("C")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = MayTinhBoTui()
    cua_so.show()
    sys.exit(app.exec_())
