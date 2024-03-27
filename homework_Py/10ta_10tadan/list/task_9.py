def odd_numbers_sorted(arr):
    odds = sorted([x for x in arr if x % 2 != 0])
    return odds, len(odds)


print(odd_numbers_sorted([3, 2, 12, 7, 6]))
