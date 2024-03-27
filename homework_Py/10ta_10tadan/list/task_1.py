number = int(input("son kiriting: "))
arr = []
counter = 0
while len(arr) <= number:
    counter += 1
    if counter % 2 != 0:
        arr.append(counter)
print(arr)