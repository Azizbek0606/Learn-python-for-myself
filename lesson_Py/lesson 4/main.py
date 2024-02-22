# task 1
# counter = 0
# for i in range(0,100,2):
#     print(i)
#     counter += 1
# print(f"1 dan 100 gacha bo'lagan sonlar ichida {counter} ta juft son bor ")

# task 2

# import random
# arr = [9, 9, 8, 9]
# hundred_num = []
# check_same = 0
# while len(hundred_num) < 100:
#     for i in range(8):
#         arr.append(random.randint(0, 9))
#     txt = "".join(str(i) for i in arr)
#     arr = [9, 9, 8, 9]
#     if txt in hundred_num:
#         check_same += 1
#     else:
#         hundred_num.append(txt)
# print(
#     f"\nTasodifiy raqamlar ichida o'xshashlari {'topilmadi' if check_same == 0 else str(check_same) + ' ta'}.\n"
# )
# print(f"Tasodifiy tanlangan raqamlar:\n{hundred_num}\n")

# print(f"tasodifiy tanlangan raqam: {hundred_num[random.randint(0 , len(hundred_num) - 1)]}")

# task 3

# a = 5
# b = 2
# while a > b:
#     a -= b
# print(f"javob: {a}")

# task 4

# a = 13
# b = 2
# counter = 0
# while a > b:
#     counter += 1
#     a -= b
# print(f"javob: {counter}")

# task 5

# a = 1000
# b = 100
# counter = 0
# while a >= b:
#     a -= b
#     counter += 1
# print(f"butun qismi: {counter}\nqoldiq: {a}")


# task 6

a = 25
b = 3
while a > b:
    a -= b
if a == 1 and a == 2:
    print(False)
else:
    print(True) 