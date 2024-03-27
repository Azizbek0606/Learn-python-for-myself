n = int(input("n ni kiriting: "))

fibonacci_sequence = [1, 1]
for i in range(2, n):
    next_element = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_element)

print(fibonacci_sequence[:n])
