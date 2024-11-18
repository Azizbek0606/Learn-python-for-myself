# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other and self.y == other

#     def __hash__(self):
#         return hash((self.x, self.y))

#     def __bool__(self):
#         print("__bool__")
#         return self.x == self.y

# pt = Point(1, 2)
# if pt:
#     print("object pt give true")
# else:
#     print("object pt give false")
# pt2 = Point(1, 2)
# print(hash(pt), hash(pt2))


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def __getitem__(self, item):
#         return self.marks[item]

#     def __setitem__(self, key, value):
#         self.marks[key] = value

#     def __delitem__(self, key):
#         del self.marks[key]


# s1 = Student("azizbek", [1, 2, 3, 4, 5, 6])
# print(s1[2])
# s1[2] = 2
# print(s1[2])
# del s1[2]
# print(s1[2])


# class Geom:
#     name = "geom"

#     def draw():
#         print("draw geom")


# class Line(Geom):
#     name = "line"

#     def draw():
#         print("draw line")


# class Circle(Geom):

#     def draw():
#         print("draw circle")


class Product:
    def __init__(self, name, product_id, quantity, price):
        self.name = name
        self.product_id = product_id
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"Product: {self.name}, ID: {self.product_id}, Quantity: {self.quantity}, Price: {self.price}"

    def __repr__(self):
        return f"Product({self.name!r}, {self.product_id!r}, {self.quantity!r}, {self.price!r})"


class WereHouse:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print("Removed product from list")

    def get_products(self):
        return self.products


product1 = Product("Laptop", "P001", 10, 2000)

warehouse = WereHouse()

warehouse.add_product(product1)

print(warehouse.get_products())
