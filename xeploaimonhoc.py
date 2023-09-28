diem = input()

diem_arr = [float(diem) for diem in diem.split()]


diem_trung_binh=(diem_arr[0] * 1 + diem_arr[1] * 1 + diem_arr[2] * 1 + diem_arr[3] * 2 + diem_arr[4] * 3
) / 8

xep_loai = "Gioi" if diem_trung_binh >= 8 else "Kha" if diem_trung_binh >= 6.5 else "Trung binh"
if diem_trung_binh >= 3.5 and diem_trung_binh < 5:
    xep_loai = "Yeu"
xep_loai = "Kem" if diem_trung_binh < 3.5 else xep_loai

print(round(diem_trung_binh, 1))
print(xep_loai)

