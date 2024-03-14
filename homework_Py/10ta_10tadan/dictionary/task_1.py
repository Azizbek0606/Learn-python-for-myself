dict_data = {'olma': 3, 'banan': 4, 'gilos': 5}
sorted_data = dict(sorted(dict_data.items(), key=lambda item: item[1]))

print(sorted_data)
