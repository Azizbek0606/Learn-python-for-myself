a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))

if a >= b:
    print("Xatolik: a < b sharti bajarilishi kerak")
else:
    yigindi = 0
    for i in range(a, b + 1):
        yigindi += i ** 2
    print(f"{a} dan {b} gacha bo'lgan sonlar kvadratlarining yig'indisi: {yigindi}")
