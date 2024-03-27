n = int(input("n ni kiriting: "))

k = 0
while n % 2 == 0:
    n //= 2
    k += 1

if n == 1:
    print(k)
else:
    print("n 2 ning darajasi emas")
