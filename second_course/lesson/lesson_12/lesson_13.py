from abc import ABC, abstractmethod
import math

# class Fruits(ABC):
#     @abstractmethod
#     def quantity(self):
#         raise NotImplementedError


# class Banana(Fruits):
#     def quantity(self):
#         print("this is quantities")


# class Apple(Fruits):
#     def quantity(self):
#         print("this is quantities")


# bn: Fruits = Banana()
# bn.quantity()

# ///////////////////////////////////////

# class Figure(ABC):
#     @abstractmethod
#     def area(self):
#         raise NotImplementedError

#     @abstractmethod
#     def perimeter(self):
#         raise NotImplementedError

#     @classmethod
#     def info(cls):
#         return cls.__name__


# class Rectangle(Figure):
#     def __init__(self, height, width):
#         self.height = height
#         self.width = width

#     def area(self):
#         return self.height * self.width

#     def perimeter(self):
#         return 2 * (self.height + self.width)


# class Circle(Figure):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * (self.radius**2)

#     def perimeter(self):
#         return 2 * math.pi * self.radius


# rect = Rectangle(10, 5)
# circ = Circle(7)

# print(f"Rectangle Area: {rect.area()}")
# print(f"Rectangle Perimeter: {rect.perimeter()}")

# print(f"Circle Area: {circ.area()}")
# print(f"Circle Perimeter: {circ.perimeter()}")

# /////////////////////////////////////////////////////////


# class Bank:

#     def __init__(self, balance: float):
#         self.__balance = balance

#     def add(self, value: float):
#         self.__balance += value
#         return f"{value} added successfully! Current balance: {self.__balance}"

#     def withdraw(self, value: float):
#         if value > self.__balance:
#             return "Insufficient funds!"
#         else:
#             self.__balance -= value
#             return f"{value} withdrawn successfully! Current balance: {self.__balance}"

#     def balance(self) -> float:
#         return self.__balance


# bk_1 = Bank(1000)

# print(bk_1.add(500))
# print(bk_1.withdraw(2000))
# print(bk_1.balance())
# print(bk_1.withdraw(1500))


class Employee:

    def work(self):
        raise NotImplementedError


class Programmer(Employee):

    def work(self): 
        print("coding")


class Designer(Employee):

    def work(self):
        print("Drawing")


class Secure(Employee):

    def work(self):
        print("secure")
