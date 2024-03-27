def even_numbers(arr):
    evens = [x for x in arr if x % 2 == 0]
    return evens, len(evens)


print(even_numbers([2, 3, 4, 5, 6]))
