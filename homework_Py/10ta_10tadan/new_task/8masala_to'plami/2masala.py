n = int(input("n ni kiriting: "))
result = []
number = 2
while len(result) < n:
    result.append(number)
    number *= 2
print(result)
