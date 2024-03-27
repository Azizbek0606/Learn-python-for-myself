 # Ikki xonali son berilgan, uning raqamlari o‘rnini almashtirish natijasida hosil bo‘lgan son chop etilsin
# son = int(input("Ikki xonali son kiriting: "))
# chap_raqam = son // 10
# ong_raqam = son % 10
# print(f"{ong_raqam}{chap_raqam}")

son = int(input("Ikki xonali son kiriting: ")[::-1])
print(son)
