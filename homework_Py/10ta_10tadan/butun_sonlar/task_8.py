a = int(input("son kiriting"))
if a <= 99 and a >= 10:
    print(f"kiritilgan son: {a}\nteskariga aylantirilgan son: {a % 10}{int(a / 10)}")