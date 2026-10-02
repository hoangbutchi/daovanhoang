danh_sach_sach = [
    {"ma_sach": "S01", "ten_sach": "Lap trinh Python co ban", "tac_gia": "Nguyen Van A", "nam_xb": 2023, "trang_thai": "Co san", "nguoi_muon": "", "so_ngay_muon": 0},
    {"ma_sach": "S02", "ten_sach": "Cau truc du lieu va giai thuat", "tac_gia": "Tran Thi B", "nam_xb": 2022, "trang_thai": "Co san", "nguoi_muon": "", "so_ngay_muon": 0},
    {"ma_sach": "S03", "ten_sach": "Co so du lieu nang cao", "tac_gia": "Le Van C", "nam_xb": 2024, "trang_thai": "Co san", "nguoi_muon": "", "so_ngay_muon": 0},
    {"ma_sach": "S04", "ten_sach": "Tri tue nhan tao nhap mon", "tac_gia": "Pham Van D", "nam_xb": 2023, "trang_thai": "Co san", "nguoi_muon": "", "so_ngay_muon": 0},
]

lich_su_tra_sach = []
PHI_MUON_MOI_NGAY = 2000

def hien_thi_danh_sach_sach():
    print("\n" + "=" * 85)
    print(f"{'Ma sach':<10}{'Ten sach':<32}{'Tac gia':<18}{'Nam':<8}{'Trang thai':<12}{'Nguoi muon':<15}")
    print("-" * 85)
    for s in danh_sach_sach:
        print(f"{s['ma_sach']:<10}{s['ten_sach']:<32}{s['tac_gia']:<18}{s['nam_xb']:<8}{s['trang_thai']:<12}{s['nguoi_muon']:<15}")
    print("=" * 85)

def tim_sach_theo_ma(ma_sach):
    for s in danh_sach_sach:
        if s["ma_sach"] == ma_sach:
            return s
    return None

def tim_kiem_sach(tu_khoa):
    ket_qua = [s for s in danh_sach_sach if tu_khoa.lower() in s["ten_sach"].lower() or tu_khoa.lower() in s["tac_gia"].lower()]
    if len(ket_qua) == 0:
        print(f"-> Khong tim thay sach nao phu hop voi tu khoa '{tu_khoa}'.")
        return
    print(f"\nKET QUA TIM KIEM CHO '{tu_khoa}':")
    for s in ket_qua:
        print(f"  [{s['ma_sach']}] {s['ten_sach']} - {s['tac_gia']} ({s['nam_xb']}) | {s['trang_thai']}")

def them_sach(ma_sach, ten_sach, tac_gia, nam_xb):
    if tim_sach_theo_ma(ma_sach) is not None:
        print(f"-> Ma sach {ma_sach} da ton tai, khong the them.")
        return
    danh_sach_sach.append({
        "ma_sach": ma_sach,
        "ten_sach": ten_sach,
        "tac_gia": tac_gia,
        "nam_xb": nam_xb,
        "trang_thai": "Co san",
        "nguoi_muon": "",
        "so_ngay_muon": 0
    })
    print(f"-> Da them sach '{ten_sach}' (Ma: {ma_sach}) thanh cong.")

def muon_sach(ma_sach, nguoi_muon, so_ngay):
    sach = tim_sach_theo_ma(ma_sach)
    if sach is None:
        print(f"-> Khong tim thay ma sach {ma_sach}.")
        return
    if sach["trang_thai"] == "Dang muon":
        print(f"-> Sach '{sach['ten_sach']}' da co nguoi muon ({sach['nguoi_muon']}), khong the muon tiep.")
        return
    sach["trang_thai"] = "Dang muon"
    sach["nguoi_muon"] = nguoi_muon
    sach["so_ngay_muon"] = so_ngay
    print(f"-> Da cho {nguoi_muon} muon sach '{sach['ten_sach']}' trong {so_ngay} ngay.")

def tra_sach(ma_sach, so_ngay_thuc_te):
    sach = tim_sach_theo_ma(ma_sach)
    if sach is None:
        print(f"-> Khong tim thay ma sach {ma_sach}.")
        return
    if sach["trang_thai"] == "Co san":
        print(f"-> Sach '{sach['ten_sach']}' hien dang co san tai thu vien, khong can tra.")
        return
    
    phi_muon = so_ngay_thuc_te * PHI_MUON_MOI_NGAY
    lich_su_tra_sach.append({
        "ma_sach": ma_sach,
        "ten_sach": sach["ten_sach"],
        "nguoi_muon": sach["nguoi_muon"],
        "so_ngay": so_ngay_thuc_te,
        "tong_tien": phi_muon
    })
    print(f"-> Nguoi doc {sach['nguoi_muon']} da tra sach '{sach['ten_sach']}'.")
    print(f"-> Thoi gian da muon: {so_ngay_thuc_te} ngay. Tong phi can thu: {phi_muon:,} VND")
    sach["trang_thai"] = "Co san"
    sach["nguoi_muon"] = ""
    sach["so_ngay_muon"] = 0

def thong_ke_thu_vien():
    tong_sach = len(danh_sach_sach)
    sach_co_san = len([s for s in danh_sach_sach if s["trang_thai"] == "Co san"])
    sach_dang_muon = tong_sach - sach_co_san
    tong_phi_thu = sum(gd["tong_tien"] for gd in lich_su_tra_sach)
    
    print("\n" + "=" * 50)
    print("THONG KE THU VIEN:")
    print(f"Tong so dau sach: {tong_sach}")
    print(f"So sach san sang cho muon: {sach_co_san}")
    print(f"So sach dang duoc muon: {sach_dang_muon}")
    print(f"Tong so luot da tra sach: {len(lich_su_tra_sach)}")
    print(f"Tong phi da thu: {tong_phi_thu:,} VND")
    print("=" * 50)

def nhap_so_nguyen(loi_nhac):
    while True:
        try:
            gia_tri = int(input(loi_nhac))
            if gia_tri > 0:
                return gia_tri
            print("-> Gia tri phai lon hon 0, vui long nhap lai.")
        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap lai mot so nguyen.")

def hien_thi_menu():
    print("\n===== HE THONG QUAN LY THU VIEN MINI =====")
    print("1. Hien thi danh sach toan bo sach")
    print("2. Tim kiem sach theo ten hoac tac gia")
    print("3. Them sach moi vao thu vien")
    print("4. Muon sach")
    print("5. Tra sach va thanh toan phi")
    print("6. Thong ke thu vien")
    print("0. Thoat chuong trinh")

def chay_chuong_trinh():
    while True:
        hien_thi_menu()
        lua_chon = input("Nhap lua chon cua ban (0-6): ").strip()
        if lua_chon == "1":
            hien_thi_danh_sach_sach()
        elif lua_chon == "2":
            tu_khoa = input("Nhap ten sach hoac tac gia can tim: ").strip()
            tim_kiem_sach(tu_khoa)
        elif lua_chon == "3":
            ma_sach = input("Nhap ma sach moi (VD: S05): ").strip().upper()
            ten_sach = input("Nhap ten sach: ").strip().title()
            tac_gia = input("Nhap ten tac gia: ").strip().title()
            nam_xb = nhap_so_nguyen("Nhap nam xuat ban: ")
            them_sach(ma_sach, ten_sach, tac_gia, nam_xb)
        elif lua_chon == "4":
            ma_sach = input("Nhap ma sach can muon: ").strip().upper()
            nguoi_muon = input("Nhap ten nguoi muon: ").strip().title()
            so_ngay = nhap_so_nguyen("Nhap so ngay du kien muon: ")
            muon_sach(ma_sach, nguoi_muon, so_ngay)
        elif lua_chon == "5":
            ma_sach = input("Nhap ma sach can tra: ").strip().upper()
            so_ngay = nhap_so_nguyen("Nhap so ngay thuc te da muon: ")
            tra_sach(ma_sach, so_ngay)
        elif lua_chon == "6":
            thong_ke_thu_vien()
        elif lua_chon == "0":
            print("Cam on ban da su dung chuong trinh quan ly thu vien. Tam biet!")
            break
        else:
            print("-> Lua chon khong hop le, vui long chon lai tu 0 den 6.")

if __name__ == "__main__":
    chay_chuong_trinh()
