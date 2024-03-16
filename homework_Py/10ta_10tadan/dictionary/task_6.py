inp_num = int(input("son kiriting: "))
main_dict = {}
for i in range(inp_num):
    main_dict.update({f"{i + 1}":i+1})
print(f"kiritilgan son: {inp_num}\nhosil qilingan lig'at: {main_dict}")