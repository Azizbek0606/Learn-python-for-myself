# def digit_count_sum(a):
#     if a > 9:
#         get_nuum_len = len(str(a))
#         count_num = 0
#         for i in str(a):
#             count_num += int(i)
#         return f"\nkiritilgan son: {a}\nraqamlar yig'indisi: {count_num}\nraqamalar soni: {get_nuum_len}\n"
#     else:
#         return "9 dan katta son kiriting"

# input_num = int(input("9 dan katta son kiriting: "))
# print(digit_count_sum(input_num))


# def count_multiple(a , b):
#     if a < b:
#         count_num = 0
#         for i in range(a , b):
#             count_num += i * i
#         return count_num
#     elif a > b:
#         return "bitinchi son ikkinchi sondan katta"
#     else:
#         return "xato malumot kiritili"

# first_num = int(input("1-soni kiriting"))
# second_num = int(input("2-soni kiriting"))
# print(count_multiple(first_num , second_num))

# def calc(a,b,op):
#     if int(op) == 1:
#         print(f"ayrma : {a - b}")
#     elif int(op) == 2:
#         print(f"ko'paytma : {a * b}")
#     elif int(op) == 3:
#         if b > 0:
#             print(f"bo'linma : {a / b}")
#     else:
#         print(f"yig'indi : {a + b}")

# while True:
#     a = int(input("1 - sonni kiriting"))
#     b = int(input("2 - sonni kiriting"))
#     c = input("qanday amal bajariladi:\n0 - dasturni to'xtatish\n1 - ayrish\n2 - ko'paytirish\n3 - bo'lish\nboshqa holda qo'shish")
#     calc(a, b, c)
#     if int(c) == 0:
#         print("dastur to'xtatildi")
#         break

son = int(input("son"))

while son % 5 == 0:
    son /= 5
print(son == 1)