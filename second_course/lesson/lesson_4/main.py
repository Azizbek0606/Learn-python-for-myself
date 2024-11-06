# class Cats:
#     name = "Alex"
#     age = 2
#     color = "white"

#     def set_name(self, name):
#         """example class function"""
#         print("call method from cats object")
#         self.name = name
#         print(f"this is {self.name}")

#     def voice(self):
#         print(f"Meow {self.name}")

#     def get_name(self):
#         return self.color, self.age ,self.name

# ct = Cats()
# getattr(ct , "name")
# setattr(ct , "age" , 40)
# ct.set_name("Sara")
# print(hasattr(ct, "color"))
# delattr(ct, "color")
# ct.voice()


class Dogs:

    name = None
    age = None
    wight = None
    breed = None

    def set_value(self, name, age, wight, breed):
        self.name = name
        self.age = age
        self.wight = wight
        self.breed = breed

        if self.wight is not None:
            self.bark()

    def get_attr(self):
        return self.name, self.age, self.wight, self.breed

    def bark(self):
        print(f"woff woff I'm {self.breed}")


dog = Dogs()
dog.set_value("Buddy", 3, 20, "German Shepherd")