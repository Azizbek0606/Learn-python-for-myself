a = int(input("a ni kiriting (a > b): "))
b = int(input("b ni kiriting (a > b): "))

if a <= b:
    print("a > b emas")
else:
    kesmalar_soni = 0
    while a >= b:
        a -= b
        kesmalar_soni += 1
    print(f"a kesmaga joylashtirilgan b kesmalar soni: {kesmalar_soni}")
