def IsSquare(k):
    return int(k**0.5) ** 2 == k


sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
kvadrat_sonlar_soni = sum(IsSquare(son) for son in sonlar)
print(kvadrat_sonlar_soni)
