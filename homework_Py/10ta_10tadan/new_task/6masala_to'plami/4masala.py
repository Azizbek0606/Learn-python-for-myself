n = int(input("n ni kiriting: "))

daraja = 3
daraja_natija = 1
while daraja_natija < n:
    daraja_natija *= daraja

if daraja_natija == n:
    print("True")
else:
    print("False")
