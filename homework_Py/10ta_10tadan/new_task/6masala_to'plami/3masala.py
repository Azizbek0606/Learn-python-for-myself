n = int(input("n ni kiriting: "))
k = int(input("k ni kiriting: "))

if k == 0:
    print("k!= 0 ")
else:
    butun_qism = 0
    qoldiq = n
    while qoldiq >= k:
        butun_qism += 1
        qoldiq -= k
    print(f"Bo'linmaning butun qismi: {butun_qism}")
    print(f"Bo'linmaning qoldiq qismi: {qoldiq}")
