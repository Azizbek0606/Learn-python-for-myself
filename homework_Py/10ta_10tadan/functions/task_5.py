def Range(a, b, c):
    if a > b:
        return 0
    else:
        counter = 0
        counter1 = 0
        for i in range(a, b + 1):
            counter += i
        for i in range(b, c + 1):
            counter1 += i
        return counter, counter1


print(Range(3 , 8 , 5))
