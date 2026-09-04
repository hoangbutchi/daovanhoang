import math

# Bai tap 4.1
print("=== Bai tap 4.1 ===")
toa_do = (3, 5)
print(toa_do, type(toa_do))

# Bai tap 4.2
print("\n=== Bai tap 4.2 ===")
x, y = toa_do
print("x =", x, "- y =", y)
a, b = 10, 20
a, b = b, a
print("a =", a, "- b =", b)

# Bai tap 4.3
print("\n=== Bai tap 4.3 ===")
c, d = 17, 5
thuong_du = divmod(c, d)
thuong, du = thuong_du
print(f"{c} chia {d} duoc thuong {thuong}, du {du}")

# Hoat dong 5
print("\n=== Hoat dong 5 ===")
diem_a = (2, 3)
diem_b = (7, 8)
xa, ya = diem_a
xb, yb = diem_b

khoang_cach = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
print(f"Khoang cach giua {diem_a} va {diem_b} la: {round(khoang_cach, 2)}")

cac_diem = [(0, 0), (3, 4), (6, 8)]
goc_o = (0, 0)
x0, y0 = goc_o
for x, y in cac_diem:
    kc = math.sqrt((x - x0) ** 2 + (y - y0) ** 2)
    print(f"Khoang cach tu ({x}, {y}) den goc toa do la: {round(kc, 2)}")
