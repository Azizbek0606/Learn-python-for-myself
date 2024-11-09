# class Point:
#     instace_count = 0
#     def __new__(cls, *args, **kwargs):
#         print("call __new__ method", args)
#         cls.instace_count += 1
#         return super().__new__(cls)

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         print(self.x, self.y)


# pt = Point(2, 4)
# pt1 = Point(2, 4)
# pt2 = Point(2, 4)
# pt3 = Point(2, 4)
# print(pt.count)


class Rectangle:

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def is_square(self):
        return self.__width == self.__height

    def resize(self, new_height, new_width):
        self.__width = new_width
        self.__height = new_height
        return "size updated"


re = Rectangle(12, 12)
print("is square:", re.is_square())
print(re.area())
print(re.perimeter())
print(re.resize(15, 17))

print("is square:", re.is_square())
print(re.area())
print(re.perimeter())
