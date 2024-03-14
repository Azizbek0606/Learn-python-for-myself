def create_new_file(index , context):
    with open(f"task_{index}.py" , "w") as file:
        file.write(context)

for i in range(10):
    create_new_file(i + 1 , f"""print("hello world{i + 1}")""")