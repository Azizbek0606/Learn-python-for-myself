narx = float(input("1 kg konfetning narxini kiriting: "))
print("1, 1.2, ..., 2 kg konfetning baholari:")
for kg in range(10, 21, 2):
    print(f"{kg / 10} kg uchun: {narx * (kg / 10)} so'm")

