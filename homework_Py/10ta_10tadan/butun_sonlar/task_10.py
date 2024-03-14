a = int(input("son kiriting"))
if a >= 100 and a <= 999:
    print(f"kiritilgan son: {a}\nbirlikalr xonasi: {int((a % 100) % 10)}\no'nliklar xonasi: {int((a % 100) / 10)}")