import random

print("Хотите узнать какой пирожок вам положен?")
a = " "
while a != "":
    a = input("Нажмите Enter чтобы продолжить ")

n = random.randint(1, 5)
if n == 1:
    print("Ваш пирожок с капустой")
elif n == 2:
    print("Ваш пирожок с вишней")
elif n == 3:
    print("Ваш пирожок с мясом")
elif n == 4:
    print("Ваш пирожок с картошкой")
else:
    print("Ваш пирожок с луком и яйцом")
