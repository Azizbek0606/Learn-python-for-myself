a = int(input("a sonini kiriting: "))
b = int(input("b sonini kiriting: "))
counter = 1
if a < b:
    for i in range(a, b + 1):
        counter *= i
else:
    print(
        "xato qiymat qayta urinib ko'ring\na soni b sonidan kichik bo'lishi shart !!!"
    )
print(counter)
