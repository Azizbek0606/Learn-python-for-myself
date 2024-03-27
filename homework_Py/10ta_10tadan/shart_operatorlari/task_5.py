a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))
c = int(input("3-sonni kiriting: "))
musbatlar_soni = 0
manfiylar_soni = 0
if a > 0:
    musbatlar_soni += 1
elif a < 0:
    manfiylar_soni += 1

if b > 0:
    musbatlar_soni += 1
elif b < 0:
    manfiylar_soni += 1

if c > 0:
    musbatlar_soni += 1
elif c < 0:
    manfiylar_soni += 1

print("Musbat sonlar soni:", musbatlar_soni)
print("Manfiy sonlar soni:", manfiylar_soni)
