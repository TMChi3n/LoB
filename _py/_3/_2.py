## cau 2

while True:
    try:
        average = eval(input('Nhap diem tb: '))
        if average < 0 or average > 10:
            print('Nhap diem tu khoang 1 -> 10')
            continue
        elif average >= 9:
            type = 'Gioi'
        elif average >= 7:
            type = 'Kha'
        elif average >= 5:
            type = 'Trung binh'
        else:
            type = 'Yeu'
        print(f'Voi diem trung binh = {average}, ban duoc xep loai {type}')
    except:
        break
print('Cook')