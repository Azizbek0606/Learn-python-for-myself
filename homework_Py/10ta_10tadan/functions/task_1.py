def check_zero(x):
    if x == 0:
        return 0
    elif x >= 0:
        return 1
    else:
        return -1

number = int(input("son kiriting: "))
print(check_zero(number))
