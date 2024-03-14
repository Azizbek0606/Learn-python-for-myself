a = int(input("son kiriting"))
if a <= 99 and a >= 10:
    print(f"yig'indisi: {int(a / 10) + (a % 10)}")
    print(f"ko'paytmasi: {int(a / 10) * (a % 10)}")