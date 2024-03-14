simple_dict1 = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4}
a = input("qiymat kiriting")
check_item = 0
for i in simple_dict1.items():
    if i.count(int(a)) >= 1:
        check_item += 1
if check_item:
    print("qiymat topildi")
else:
    print("bunday qiymat majud emas")