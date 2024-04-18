from abc import ABC, abstractmethod


# class Shakl(ABC):
#     @abstractmethod
#     def yuzi(self):
#         pass

#     def perimetr(self):
#         pass


# class Uchburchak(Shakl):

#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def yuzi(self):
#         p = (self.a + self.b + self.c) / 2
#         s = p * (p - self.a) * (p - self.b) * (p - self.c) ** 1/2
#         return s
#     def perimetr(self):
#         return self.a + self.b + self.c

# class Tortburchak(Shakl):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def yuzi(self):
#         return self.a * self.b
#     def perimetr(self):
#         return (self.a + self.b) * 2


# uchburchak = Uchburchak(12,12,20)
# print(f"uchburchak yuzi: {uchburchak.yuzi()}")
# print(f"uchburchak perimetr: {uchburchak.perimetr()}")


# tortburchak = Tortburchak(12,12)
# print(f"tortburchak yuzi: {tortburchak.yuzi()}")
# print(f"tortburchak perimetr: {tortburchak.perimetr()}")


class CalMethod(ABC):
    @abstractmethod
    def plus(self):
        pass

    @abstractmethod
    def minus(self):
        pass

    @abstractmethod
    def kopaytirish(self):
        pass

    @abstractmethod
    def bolish(self):
        pass

    @abstractmethod
    def daraja(self):
        pass


class Calculator(CalMethod):

    def event(self, a, b, c):
        if c == "k":
            self.kopaytirish(a, b)
        elif c == "b":
            self.bolish(a, b)
        elif c == "a":
            self.minus(a, b)
        elif c == "q":
            self.plus(a, b)
        elif c == "d":
            self.daraja(a, b)
        elif c == "x":
            exit(0)
        else:
            print(f"Error: {c} is not a valid input")

    def plus(self, a, b):
        print(a + b)

    def minus(self, a, b):
        print(a - b)

    def kopaytirish(self, a, b):
        print(a * b)
    def daraja(self, a, b):
            print(a**b)

    def bolish(self, a, b):
        print(a / b)

    

    def calculate(self, a, b, c):
        self.event(a, b, c)


calculator = Calculator()

a = int(input("Enter the number of a"))
b = int(input("Enter the number of b"))
c = input("K - kopaytirish\nB - bolish\nq - qo'shish\na - ayrish\nd - daraja\nx - dasturni to'xtatish")
  
calculator.calculate(a, b, c)