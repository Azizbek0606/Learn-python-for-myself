a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))
n = b - a - 1

print("a va b orasidagi sonlar:")
for i in range(b - 1, a, -1):
    print(i, end=" ")

print("\na va b orasidagi sonlar miqdori:", n)

