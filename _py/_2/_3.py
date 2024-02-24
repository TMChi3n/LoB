# cau 3
s1 = 'Obama'
s2 = 'Chien Tran'
# cach 1
print(f'{s1: ^20}')
print(f'{s2: ^30}')
# cach 2: qua phai
print(f'{s1.rjust(20, "-")}')
print(f'{s2.rjust(30, "-")}')
# cach 3: qua trai
print(f'{s1.ljust(20, "-")}')
print(f'{s2.ljust(30, "-")}')
# cach 4: giua
print(f'{s1.center(20, "-")}')
print(f'{s2.center(30, "-")}')