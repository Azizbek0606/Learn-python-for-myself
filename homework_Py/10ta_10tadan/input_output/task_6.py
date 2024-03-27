input_number = int(input("son kiriting: "))
input_number1 = int(input("son kiriting: "))
input_number2 = int(input("son kiriting: "))
v = input_number * input_number1 * input_number2
s = 2 * (
    input_number * input_number2
    + input_number * input_number1
    + input_number1 * input_number2
)
print(v)
print(s)
