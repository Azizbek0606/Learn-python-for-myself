def RootsCount(a, b, c):
    D = b**2 - 4 * a * c 
    if D > 0:
        return 2
    elif D == 0:
        return 1
    else:
        return 0

tenglama1 = RootsCount(1, -5, 6 ) 
tenglama2 = RootsCount(1, -4 ,4 ) 
tenglama3 = RootsCount(1,  4,  6 )  
print(tenglama1)
print(tenglama2)
print(tenglama3)