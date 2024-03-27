n = int(input("n ni kiriting: "))
a = []

print("Massivni elementlarini kiriting:")
for i in range(n):
    a.append(int(input()))

odd_count = 0
print("Toq sonlar: ", end="")
for i in range(n):
    if a[i] % 2 != 0:
        print(a[i], end=" ")
        odd_count += 1

print("\nToq sonlar miqdori:", odd_count)
