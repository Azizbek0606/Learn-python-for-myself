n = int(input("n ni kiriting: "))
a = []

print("Massivni elementlarini kiriting:")
for i in range(n):
    a.append(int(input()))

even_count = 0
print("Juft sonlar: ", end="")
for i in range(n):
    if a[i] % 2 == 0:
        print(a[i], end=" ")
        even_count += 1

print("\nJuft sonlar miqdori:", even_count)
