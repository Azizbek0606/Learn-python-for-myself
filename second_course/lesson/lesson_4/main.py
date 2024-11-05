class Cats:
    name = "Alex"
    age = 2
    color = "white"

    def set_name(self):
        """example class function"""
        print("call method from cats object")

ct = Cats()
ct_2 = Cats()
ct.name = "Sara"
print(ct.name, ct.__dict__)