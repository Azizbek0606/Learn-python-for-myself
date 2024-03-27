def fibonacci(n):
    fib_seq = [1, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[:n]


print(fibonacci(6))
