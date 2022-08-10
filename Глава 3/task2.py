import random

orel = 0
reshka = 0
input("Давайте подбросим монетку 100 раз, а я скажу, сколько раз выпал орел, а сколько решка. ")

for i in range(100):
    n = random.randint(1, 2)
    if n == 1:
        orel += 1
    else:
        reshka += 1

print(f"Орел выпал {orel} раз(а), а решка {reshka} раз(а).")