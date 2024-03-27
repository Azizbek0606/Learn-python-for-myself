def Quarter(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4

print(Quarter(2, 3))
print(Quarter(-2, 3))
print(Quarter(2, -3))
