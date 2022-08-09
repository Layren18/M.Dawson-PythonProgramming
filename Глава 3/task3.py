import random

print("Угадай число")
print("Я загадал число от 1 до 100.")
print("Попробуйте его отгадать за наименьшее кол-во попыток.\n")

the_number = random.randint(1, 100)
guess = int(input("Назовите число: "))
tries = 1

while guess != the_number:
    if guess > the_number:
        print("Меньше...")
    else:
        print("Больше...")

    guess = int(input("Назовите число: "))
    tries += 1

print("Вы отгадали! Это действительно число", the_number)
print("И вы это сделали за ", tries, "попыток!") 