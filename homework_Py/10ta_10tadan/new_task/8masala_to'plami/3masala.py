a = int(input("Arifmetik progressiyaning birinchi hadni kiriting: "))
d = int(input("Ayirmasini kiriting (d): "))
n = int(input("n hadini kiriting: "))

progression = [i * d + a for i in range(n)]
print(progression)
