a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))

if a >= b:
    print("Xatolik: a < b sharti bajarilishi kerak")
else:
    kopaytma = 1
    for i in range(a, b + 1):
        kopaytma *= i
    print(f"{a} dan {b} gacha bo'lgan sonlar ko'paytmasi: {kopaytma}")
