"""Hoat dong 5: Requests - goi API cong khai, xu ly du lieu JSON."""
import requests

# --- 5.1 Goi API GitHub va doc JSON ---
print("=== 5.1 API GitHub: python/cpython ===")
try:
    response = requests.get("https://api.github.com/repos/python/cpython", timeout=10)
except requests.RequestException as loi:
    print("Khong ket noi duoc toi API:", loi)
else:
    if response.status_code == 200:
        du_lieu = response.json()
        print("Ten repository:", du_lieu["full_name"])
        print("So luot gan sao (stars):", du_lieu["stargazers_count"])
        print("Ngon ngu chinh:", du_lieu["language"])
    else:
        print("Goi API that bai, ma loi:", response.status_code)

# --- 5.2 Goi API ty gia ngoai te ---
print("\n=== 5.2 Ty gia USD -> VND ===")
try:
    response = requests.get("https://open.er-api.com/v6/latest/USD", timeout=10)
except requests.RequestException as loi:
    print("Khong ket noi duoc toi API ty gia:", loi)
else:
    if response.status_code == 200:
        du_lieu = response.json()
        ty_gia_vnd = du_lieu["rates"]["VND"]
        print(f"1 USD = {ty_gia_vnd:,.0f} VND")
        print("Cap nhat luc:", du_lieu.get("time_last_update_utc", "khong ro"))
    else:
        print("Khong lay duoc ty gia, ma loi:", response.status_code)
