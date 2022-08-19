# Анаграммы
# Компьютер выбирает рандомное слово и делает из него анаграмму
# Пользователю нужно угадать исходное слово

import random
# создаем константу со словами
WORDS = ("питон", "легко", "сложно", "ответ", "ксилофон", "молоток", "вопрос", "клавиатура")
# выбираем случайный элемент
word = random.choice(WORDS)

correct = word

# создаем анаграмму
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# начинаем игру
print(
    """
               Добро пожаловать в Анаграммы!
    
       Восстановите порядок букв, чтобы получить слово.
    """
)
print("Анаграмма:", jumble)

guess = input("\nВведите исходное слово: ")
while guess != correct and guess != "":
    print("Неверно.")
    guess = input("Введите исходное слово: ")

if guess == correct:
    print("Это оно! Вы угадали!\n")

print("Спасибо за игру.")

input("\n\nНажмите Enter чтобы выйти.")