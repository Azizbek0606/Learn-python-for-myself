def circleS(x, y, z):
    arr = [x, y, z]
    arr1 = []
    for i in arr:
        arr1.append(round(3.14159 * i**2 , 2))
    return arr1

print(circleS(10 , 100 , 1))
