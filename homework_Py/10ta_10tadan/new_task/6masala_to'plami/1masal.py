a = int(input("a ni kiriting (a > b): "))
b = int(input("b ni kiriting (a > b): "))

if a <= b:
    print("a > b emas ")
else:
    qolgan_uzunlik = a
    while qolgan_uzunlik >= b:
        qolgan_uzunlik -= b
    print(f"Qolgan bo'lagning uzunligi: {qolgan_uzunlik}")
