## cau 1
Chuoi = 'Lap trinh Python'
soNguyen = 123445678
soThuc = 2564.32142
soPhuc = 453.2 + 5.8j
phanTram = 0.983452123431141318984947593
soTT = 1
print(f'Bien chuoi  co gia tri la: {Chuoi}, sau khi su dung phuong thuc title la: {Chuoi.title()}')
print(f'Bien So Nguyen  co gia tri la: {soNguyen:,}')
print(f'Bien chuoi  co gia tri la: {soPhuc:,.2f}')
print(f'Bien chuoi  co gia tri la: {soPhuc}, trong do:')
print(f'- Phan thuc la: {soPhuc.real}')
print(f'- Phan ao la: {soPhuc.imag}')
print(f'Phan tram co gia tri la: {phanTram:.2%}')
print(f'Bien chuoi  co gia tri la: {soTT}, sau khi dinh dang voi 3 chu so: {soTT:0>3}')