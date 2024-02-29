# def calculate(x , y , z):
#     if z == "+":
#         return x + y
#     elif z == "-":
#         return x - y
#     elif z == "/":
#         return x / y
#     elif z == "*":
#         return x * y
#     else:
#         return "xatlik fqat + , - , / , * belgilrini kiriting"

# num1 = int(input("1 - son"))
# num2 = int(input("2 - son"))
# event = input("qandy amal bajarish kerak")
# print(calculate(num1, num2, event))

# arr = [1,2,3,5,3,4,5,8,9]
# min(arr)
# def get_max_min(arr):
#     arr.sort()
#     print(f"katta qiymat: {arr[0]} , kichik qiymat: {arr[-1]}")
# get_max_min(arr)


# def find_max_min(x,y):
#     if x > y:
#         return f"{x} katta {y} kichik"
#     elif x < y:
#         return f"{y} katta {x} kichik"
#     else:
#         return "ikkala son teng"

# x = int(input("1 - sonni kiriting"))
# y = int(input("2 - sonni kiriting"))
# print(find_max_min(x , y))


# task 1

def sing(x:int):
    if int(x) > 0:
        return 1
    elif int(x) < 0:
        return -1
    elif int(x) == 0:
        return 0
    else:
        return "xato qiymat"

x = input("son:\n")
print(sing(x))

# print(True if x > 0 else False)