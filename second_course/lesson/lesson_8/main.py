# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def __call__(self):
#         return self.x , self.y

# pt = Point(12 ,12)


# def __new__()

# def __init()


# staticmethod


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     @staticmethod
#     def area(r):
#         return 3.14 * r * r


# pt = Point(1, 3)
# print(pt.area(3))


# class Students:
#     counter = 0
#     def __init__(self, name):
#         self.name = name
#         Students.counter += 1

#     @classmethod
#     def get_count(cls):
#         return cls.counter

# s1 = Students('John')
# s2 = Students('Alice')

# print(Students.get_count())


class Counter:
    counter = 0
    instance_values = []

    @classmethod
    def show_count(cls):
        return f"Current count: {cls.counter}"

    def __call__(self, *args):
        Counter.counter += 1
        Counter.instance_values.append(args[0])
        print( sum(Counter.instance_values))


ct = Counter()
ct(3)
ct(4)
ct(6)

print(ct.show_count())
