# cau 2
while True:
    a = input('Nhap a (Nhap 0 de thoat): ')
    if (int(a) == 0):
        break
    if not a.isdigit():
        print('Vui long nhap so')
        continue
    while True:
        b = input('Nhap b (b > 0): ')
        if not b.isdigit() or int(b) == 0:
            print('Vui long nhap so > 0')
            continue
        break
    a = int(a)
    b = int(b)
    print(f'Thuong so cua a va b: {a/b}:.2f')
    print(f'Thuong so cua a va b (chi lay phan nguyen): {a//b}')
    print(f'Thuong so cua a va b (chi lay phan du): {a%b}')
print("end")