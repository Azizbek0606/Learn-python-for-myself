a = int(input("birinchi son: "))
d = int(input("ayirma: "))
n = int(input("hadlar soni: "))
progressiya = [a + i * d for i in range(n)]
print(progressiya)