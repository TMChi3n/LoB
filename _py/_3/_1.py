## cau 1

while True:
    try:
        average = eval(input('Nhap diem tb: '))
        if average < 0 or average > 10:
            print('Nhap diem tu khoang 1 -> 10')
            continue
        if average >= 5:
            print('Ban da vuot qua ki thi')
        else:
            print('Ban da truot')
        Next = input('Ban co tiep tuc khong (c/k): ')
        if Next.lower() == 'k': break
    except:
        print('Xin vui long nhap lai')