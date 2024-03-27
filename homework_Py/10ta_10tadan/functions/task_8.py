def Even(k):
    return k % 2 == 0


sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
juft_sonlar_soni = sum(Even(son) for son in sonlar)
print(juft_sonlar_soni) 
