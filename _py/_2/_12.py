while True:
    Chuoi = input('Nhap mot chuoi (Empty for exit): ')
    if Chuoi.strip() == '': break
    ChuoiBD = input('Nhap chuoi bat dau (muon kiem tra): ')
    if Chuoi.startswith(ChuoiBD):
        print(f'{Chuoi} bat dau voi chuoi {ChuoiBD}')
    else :
        print(f'{Chuoi} chuoi khong bat dau voi chuoi {ChuoiBD}')