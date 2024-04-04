# class Calculator:
#     __x = 3
#     __y = 4

#     def getter(self):
#         return self.__x

#     def setter(self, value):
#         self.__y = value

#     def calculate(self):
#         return self.__plus()

#     def __plus(self):
#         return self.__x + self.__y

# new_number = Calculator()
# print(new_number.getter())
# new_number.calculate()
# new_number.setter(5)
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rectangle = Rectangle(10, 20)
print(f"Rectangle area: {rectangle.area()}")
print(f"Rectangle perimeter: {rectangle.perimeter()}")
