narx = float(input("1 kg konfetning narxini kiriting: "))
print("0.1, 0.2, ..., 1 kg konfetning baholari:")
for kg in range(1, 11):
    print(f"{kg / 10} kg uchun: {narx * (kg / 10)} so'm")
