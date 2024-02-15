retake = ["Maruf", "Duryodbek", "Axmadsher", "Muhammadamin", "Shohjahon", "Ibrohim"]
remudle_web = []
remudle_prog = []

while True:
    print(
        "1 - index bo'ycha o'chirish\n2 - qiymat bo'yicha o'chirish\n3 - dasturni to'xtatish"
    )
    input_num = int(input("\nFaqat son kiriting:\n "))
    if input_num == 1:
        print(f"reatkega qolganlar: {retake} o'chirish uchun:")
        input_index = int(
            input(f"0 dan {len(retake) - 1}gacha hohlagan bitta index kiriting: ")
        )
        if input_index < len(retake):
            remudle_web.append(retake[input_index])
            retake.pop(input_index)
            print("retakedan imtihon o'tganlar:\n")
            for i in retake:
                print(i)

            print("\nremudlega qolganlar: \n")
            for i in remudle_web:
                print(i)
        else:
            print("Noto'g'ri index, qayta urinib ko'ring!")
    elif input_num == 2:
        for i in retake:
            print(i)
        print("\nremudlega qoldirish uchun yuqoridagi ismlardan birini kiriting\n")
        input_name = input()
        if input_name in retake:
            remudle_prog.append(input_name)
            retake.remove(input_name)
            print("retakedan imtihon o'tganlar:")
            for i in retake:
                print(i)

            print("remudlega qolganlar: ")
            for i in remudle_prog:
                print(i)
        else:
            print("\nIsm xato kiritildi, qayta urinib ko'ring\n")
    elif input_num == 3:
        print("Dastur to'xtatildi")
        break
    else:
        print("Noto'g'ri qiymt, qayta urinib ko'ring")


# num_a = int(input("birinchi son"))
# num_b = int(input("ikkinchi son"))
# num_c = int(input("uchinchi son"))

# if num_a > num_b and num_a > num_c:
#     print(f"{num_a} , {num_b} , {num_c} sonlarni ichida kattasi")
#     print(num_a)
# elif num_b > num_a and num_b > num_c:
#     print(f"{num_a} , {num_b} , {num_c} sonlarni ichida kattasi")
#     print(num_b)
# else:
#     print(f"{num_a} , {num_b} , {num_c} sonlarni ichida kattasi")
    # print(num_c)


# input_num = int(input("4 sonagacha bo'lgan son kiriting"))
# if input_num <= 9999:
#     if input_num > 0 and input_num <= 9:
#         print("kiritilga son bir xonali")
#     elif input_num >= 10 and input_num <= 99:
#         print("kiritilga son ikki xonali")
#     elif input_num >= 100 and input_num <= 999:
#         print("kiritilga son uch xonali")
#     elif input_num >= 1000 and input_num <= 9999:
#         print("kiritilga son to'rt xonali")

