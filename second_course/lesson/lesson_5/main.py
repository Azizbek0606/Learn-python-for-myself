# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         print("Call __init__ in Point")

#     def __del__(self):
#         print("call __del__")

#     def aggregate_function(self):
#         print("call aggregate function in point")


# pt = Point(1, 2)
# pt.aggregate_function()


class Rectangle:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimetr(self):
        return 2 * (self.height + self.width)


re = Rectangle(15, 25)
print(re.area())
print(re.perimetr())
