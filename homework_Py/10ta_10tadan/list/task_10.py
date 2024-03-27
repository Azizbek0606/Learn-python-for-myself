def index_sort_even_odd(arr):
    even_indices = [i for i, x in enumerate(arr) if x % 2 == 0]
    odd_indices = [i for i, x in enumerate(arr) if x % 2 != 0][::-1]
    return even_indices + odd_indices

print(index_sort_even_odd([7, 4, 7, 3, 5, 10])) 
