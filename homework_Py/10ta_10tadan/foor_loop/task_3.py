a = int(input("a son kiriting"))
b = int(input("b son kiriting"))
count = 0
if b > a:
    for i in range(b , a - 1 , -1):
        count += 1
        print(f"sonlar: {i}")
print(f"sonlar soni: {count}")