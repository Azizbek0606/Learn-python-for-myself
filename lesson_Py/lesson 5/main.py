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

# def sing(x:int):
#     if int(x) > 0:
#         return 1
#     elif int(x) < 0:
#         return -1
#     elif int(x) == 0:
#         return 0
#     else:
#         return "xato qiymat"

# x = input("son:\n")
# print(sing(x))

# print(True if x > 0 else False)


# class Car:

#     def __init__(self, model, color, position):
#         self.model = model
#         self.color = color
#         self.position = position

#     def __str__(self):
#         return f"\nmashina modeli: {self.model}\nrangi: {self.color}\npozitsiyasi: {self.position}\n"

#     def rasxod(self):
#         if self.model == "Malibu":
#             return 10
#         elif self.model == "Onix":
#             return 8
#         elif self.model == "Nexia-3":
#             return 9
#         else:
#             return "bunday turdagi mashina mavjud emas"

# car1 = Car("Onix" , "qora" , 3)
# car2 = Car("Malibu", "oq", 2)
# car3 = Car("Nexia-3" , "qora" , 4)
# print(car1)
# print(car2)
# print(car3)
# print(car1.rasxod())


# class Calculate:
#     def __init__(self , x, y):
#         self.x = x
#         self.y = y

#     def plus(self):
#         return self.x + self.y

#     def minus(self):
#         return self.x - self.y

#     def kopaytirish(self):
#         return self.x * self.y

#     def bolish(self):
#         return self.x / self.y

# num1 = int(input("1 - son: "))
# num2 = int(input("2 - son: "))
# calc1 = Calculate(num1 , num2)
# print(calc1.plus())

import math

class GetArea:
    def __init__(self , x , y , z):
        self.x = x
        self.y = y
        self.z = z

    def area(self):
        return self.x + self.y + self.z
    def yuza(self):
        half_area = int(self.area()) / 2
        return math.sqrt(
            half_area
            * (half_area - self.x)
            * (half_area - self.y)
            * (half_area - self.z)
        )

triangle = GetArea(12,12,6)
print(triangle.yuza())
print(triangle.area())
