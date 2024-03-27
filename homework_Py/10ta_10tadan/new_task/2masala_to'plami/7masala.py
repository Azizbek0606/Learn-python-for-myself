# Ikki xonali son berilgan, uning raqamlari yig’indisi va ko’paytmasi topilsin
son = int(input("Ikki xonali son kiriting: "))
chap_raqam = son // 10
ong_raqam = son % 10
yigindi = chap_raqam + ong_raqam
kopaytma = chap_raqam  * ong_raqam
print(yigindi)
print(kopaytma)