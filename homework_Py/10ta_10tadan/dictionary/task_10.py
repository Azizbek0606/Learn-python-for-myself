main_dict = {}
inp_txt = input("matn kiriting: ")
arr = [x for x in inp_txt]
for i in range(len(arr)):
    main_dict.update({arr[i]:arr.count(arr[i])})
print(main_dict)