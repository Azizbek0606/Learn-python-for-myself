def IsPowerS(k):
    while k % 5 == 0 and k != 0:
        k /= 5
    return k == 1


sonlar = [1, 5, 10, 25, 125, 625, 3125, 15625, 2, 3]
beshning_darajalari_soni = sum(IsPowerS(son) for son in sonlar)
print(beshning_darajalari_soni)
