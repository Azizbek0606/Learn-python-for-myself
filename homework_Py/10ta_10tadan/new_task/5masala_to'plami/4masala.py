
narx = float(input("1 kg konfetning narxini kiriting: "))
print("1, 2, ..., 10 kg konfetning baholari:")
for kg in range(1, 11):
    print(f"{kg} kg uchun: {narx * kg} so'm")
