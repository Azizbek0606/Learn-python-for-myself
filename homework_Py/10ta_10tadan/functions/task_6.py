def Calc(a, b, op = 4):
    if op == 1:
        return a - b
    elif op == 2:
        return a * b
    elif op == 3:
        return a / b
    else:
        return a + b

a = 10
b = 5
print(Calc(a, b, 1))
print(Calc(a, b, 2))
print(Calc(a, b, 3))
print(Calc(a, b))
