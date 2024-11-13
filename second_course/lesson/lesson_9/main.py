# class Student:
#     def __init__(self,name):
#         self.name = name


#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"

#     def __str__(self):
#         return f"{self.name}"

# st = Student("Alex")
# st
# print(st)


# class Point:
#     def __init__(self, *args):
#         self.__coords = args

#     def __len__(self):
#         return len(self.__coords)


# pt = Point(1, 2, 3, 4, 5, 6)
# print(len(pt))


# list1 = [1,2,3,-4,-6,-7,-15]
# res = list(map(abs, list1))
# print(res)


# class Point:
#     def __init__(self, *args):
#         self.__coords = args

#     def __abs__(self):
#         return list(map(abs, self.__coords))

# pt = Point(-1,2,-4,-3,8,-5,6,-7)
# print(abs(pt))


class Number:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)

    def __repr__(self):
        return f"{self.__class__}: {self.num}"

    def __len__(self):
        return len(str(abs(self.num)))

    def __abs__(self):
        return abs(self.num)


nr = Number(-5)
print(len(nr))
