from datetime import date
import random

car_number = []
penalti = []
nothing = []
a = date.today().day
b = "toq kun " if a % 2 != 0 else "juft kun"


for i in range(random.randint(10, 100)):
    car_number.append(random.randint(100, 999))

for i in car_number:
    if a % 2 == 0 and i % 2 == 0:
        nothing.append(i)
    elif a % 2 != 0 and i % 2 != 0:
        nothing.append(i)
    else:
        penalti.append(i)

print(f"\n\n\nBugun {b} jarima olganlar: ")
print(penalti)
print("\n\n\nJarima olmaganlar: ")
print(nothing)


car_num = int(input("mashina raqami"))
future_day = int(input("kun"))
future_month = int(input("oy"))
future_year = int(input("yil"))
if future_year >= 2024 and future_month >= 2 and future_day > 8:
    if future_day <= 31 and future_month <= 12 and future_year >= 2024:
        if (future_day <= 31 and future_month <= 12 and future_year >= 2024 ) and (future_day % 2 == 0 and car_num % 2  == 0):
            print(f"siz {future_day}/{future_month}/{future_year} kunida avtomobilda harakatlana olasiz")
        elif (future_day <= 31 and future_month <= 12 and future_year >= 2024 ) and (future_day % 2 != 0 and car_num % 2  != 0):
            print(f"siz {future_day}/{future_month}/{future_year} kunida avtomobilda harakatlana olasiz")
        else:
            print(f"siz {future_day}/{future_month}/{future_year} kunida avtomobilda harakatlana olmaysiz")
    else:
        print("sana xato kiritildi")
else:
    print("biz kelajak uchun ishlaymiz !!!")