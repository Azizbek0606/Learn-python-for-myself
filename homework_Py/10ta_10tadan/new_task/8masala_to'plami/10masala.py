n = int(input("n ni kiriting: "))
a = []

print("Massivni elementlarini kiriting:")
for i in range(n):
    a.append(int(input()))

even_indices = []
odd_indices = []

for i in range(n):
    if a[i] % 2 == 0:
        even_indices.append(i)
    else:
        odd_indices.insert(0, i)

sorted_indices = even_indices + odd_indices

print("Juft sonlarning indekslari o'sish tartibida:")
for index in sorted_indices:
    print(index, end=" ")

print("\nToq sonlarning indekslari kamayish tartibida:")
for index in reversed(odd_indices):
    print(index, end=" ")

print("\nMassiv:")
for index in sorted_indices:
    print(a[index], end=" ")
