def geometrik_progressiya(b, q, n):
    return [b * q**i for i in range(n)]


print(geometrik_progressiya(2, 6, 3))
