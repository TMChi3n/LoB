## 1. Tính WәQJ S 1 + 2 + 3 + … + (n-1) + n EҵQJ hai cách while và for.


S = 0
n = int(input('Nhap n: '))
i=1
# while i<=n:
#     S += i
#     i+=1

# print(S)

for i in range(1, n+1):
    S+=i

print(S)
