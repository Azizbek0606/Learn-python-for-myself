class Cats:
    name = "Alex"
    age = 2
    color = "white"

    def set_name(self, name):
        """example class function"""
        print("call method from cats object")
        self.name = name
        print(f"this is {self.name}")

    def voice(self):
        print(f"Meow {self.name}")

ct = Cats()
ct.set_name("Sara")
ct.voice()