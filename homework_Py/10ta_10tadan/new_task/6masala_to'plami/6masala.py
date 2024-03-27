n = int(input("n ni kiriting: "))

result = 1
if n % 2 == 0:
    start = 2
else:
    start = 1

while n >= start:
    result *= n
    n -= 2

print("Natija:", result)
