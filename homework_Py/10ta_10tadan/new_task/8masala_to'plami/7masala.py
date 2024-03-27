n = int(input("n ni kiriting: "))
a = []

print("Massivni elementlarini kiriting:")
for i in range(n):
    a.append(int(input()))

print("Teskari tartibda chiqarilgan massiv:")
for i in range(n - 1, -1, -1):
    print(a[i], end=" ")
