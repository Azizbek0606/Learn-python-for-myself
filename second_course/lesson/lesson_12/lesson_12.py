# class Human:
#     def voice(self):
#         raise NotImplementedError(self.__class__.__name__)


# class Student(Human):
#     def __init__(self, name: str):
#         self.name = name

#     def voice(self):
#         print("student voice")


# class Teacher(Human):
#     def __init__(self, name: str):
#         self.name = name

#     def voice(self):
#         print("teacher voice")


# class Director(Human):

#     def __init__(self, name: str):
#         self.name = name


# s1 = Student("John")
# s2 = Student("Kevin")
# t1 = Teacher("Jane")
# t2 = Teacher("Mary")
# d1 = Director("Mark")
# d2 = Director("Anita")

# humanslist = [s1, t1, t2, d2, s2]

# for human in humanslist:
#     human.voice()


# class Animal:

#     def speak(self):
#         raise NotImplementedError(self.__class__.__name__)

#     def move(self):
#         raise NotImplementedError(self.__class__.__name__)


# class Dog(Animal):
#     def speak(self):
#         print("Woof!")

#     def move(self):
#         print("Run!")


# class Cat(Animal):
#     def speak(self):
#         print("Meow!")

#     def move(self):
#         print("walk!")


# class Bird(Animal):
#     def speak(self):
#         print("Chirp!")

#     def move(self):
#         print("Fly!")


# d = Dog()
# c = Cat()
# b = Bird()
# animals_list = [d, b, c]


# def animals_behavior(behavior):
#     for i in behavior:
#         i.speak()
#         i.move()


# animals_behavior(animals_list)