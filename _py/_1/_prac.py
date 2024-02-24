# print
'''print("Hello guys!")'''

# input then print
'''inp_name = input("Ho va ten cua ban: ")
print("Hello", inp_name, sep='🙌')  # sep=' ': insert in comment'''

# data type
'''a = 5
b = 'Chien'
print("Type of a: ", type(b))'''

# pow 2 and 3
'''inp_x = int(input("Nhap x: "))   Parse data type
print("Luy thua x =", pow(inp_x, 3))    # pow : inp_x ** 3
print("Luy thua x =", float(pow(inp_x, 2, 3))) # pow: inp_x ** 2 % 3'''

'''while True :
    x = input("Nhap x (nhap 0 de ket thuc):")
    if not x.isdigit():
        print("Xin nhap so")
        continue        
    x = int(x)
    if x == 0 : break
    binhPhuong = x ** 2
    lapPhuong = x ** 3
    print(f'Binh phuong cua {x} la: {binhPhuong}')          # f : float
    print(f'Lap phuong cua {x} la: {lapPhuong}')            # {x} la x
print("Ket thuc chuong trinh...")'''

# for loop

'''for i in range(20) :
    print("*", end(''))
for j in range(50) :
    print("=")'''

'''print('*' * 20, '=' * 50, sep='\n')'''

# input math, physics, chemistry and output point and average
'''math = int(input("Nhap diem toan: "))
physics = int(input("Nhap diem vat ly: "))
chemistry = int(input("Nhap diem hoa hoc: "))
print("Diem toan, ly, hoa:", math, physics, chemistry)
print("Diem trung binh :", (math + physics + chemistry) / 3)'''

# P and S circle
'''import math

r = float(input("Nhap r: "))
print("Chu vi:", float(2 * (math.pi) * r))
print("Dien tich:", float(pow(r, 2) * (math.pi)))'''


# time 
t = int(input("Nhap t: "))
gio = t // 3600
phut = (t%3600) // 60
giay = (t%3600) % 60

print(f'{gio}')
print(f'{phut}')
print(f'{giay}')
