import datetime

# Task 2
# input_num = int(input("Og'irlikni gramda kiriting: "))
# print(f"kiritilgan massa: {input_num / 1000} kg")

# Task 3
# input_num = int(input("o'lchamni bayt ko'rinishida kiriting: "))
# print(f"kiritilgan o'lcham: {input_num / 1024} kb")

# Task 4
# a = int(input("a uchun son kiriting: "))
# b = int(input("b uchun son kiriting: "))
# print(f"a kesma {int(a / b)} ta b kesmadan tashil topgan hamda {a % b } sm ga uzun")

# ///////////////////////////////////////////////
# Task 2

user_day = int(input("tug'ilgan kuningiz"))
user_mounth = int(input("tug'ilgan oyingiz"))
user_year = int(input("tug'ilgan yilingiz"))

birthday = datetime.datetime(user_year, user_mounth, user_day)
find_now_1 = datetime.datetime.now()
print(find_now_1 - birthday)
