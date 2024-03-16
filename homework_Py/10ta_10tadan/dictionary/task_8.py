main_dict = {"first": 1, "second": 2, "third": 3, "fourth": 7}
inp_key = input("kalit kiriting: ")
was_found = False
for i in main_dict.keys():
    if inp_key == i:
        main_dict.pop(i)
        was_found = True
        break
    else:
        was_found = False
if was_found:
    print(f"kalit bo'yicha qiymat o'chirildi\nyangilangan lug'at: {main_dict}")
else:
    print("kalit xato kiritildi")