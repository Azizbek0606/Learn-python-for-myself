def custom_sequence(n, a, b):
    sequence = [a, b]
    for i in range(2, n):
        sequence.append(sum(sequence))
    return sequence


print(custom_sequence(5, 3, 4))
