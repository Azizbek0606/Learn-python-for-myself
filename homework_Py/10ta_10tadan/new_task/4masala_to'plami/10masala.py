# Ikki butun sonni kiritish
a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))

# Teng bo'lmagan holatda qiymatlar yig'indisini topish
if a != b:
    a += b
else:
    a = 0
    b = 0

# Natijaviy qiymatlarni chiqarish
print("a ning qiymati:", a)
print("b ning qiymati:", a)
