while True:
    try:
        month = int(input('Nhap thang: '))

        if month < 1 or month > 12:
            print('Chi nhap thang trong khoang 1 - 12')
            continue
        if month in (1, 3, 5, 7, 8, 10, 12):
            print(f'Thang {month} co 31 ngay')
        elif month in (4, 6, 9, 11):
            print(f'Thang {month} co 30 ngay')
        else:
            while True:
                year = input('Nhap nam: ')
                if year.isdigit():
                    year = int(year)
                    break
            if (year%400 == 0) or (year%4 == 0 and year%100 != 0):
                print(f'Thang {month} nam {year} co 29 ngay')
            else:
                print(f'Thang {month} nam {year} co 28 ngay')
    except:
        break
print('Cook')
