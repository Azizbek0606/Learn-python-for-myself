def ringS(r1, r2):
    s_tashqi = 3.14159 * r1**2
    s_ichki = 3.14159 * r2**2
    return round(s_tashqi - s_ichki , 2)


print(ringS(4, 2))
print(ringS(2, 1))
print(ringS(3, 2))
