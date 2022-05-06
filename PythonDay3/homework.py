# Цикл
# Создать список из десяти целых чисел.
# Вывести на экран каждое число, увеличенное на 1.

# range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for number in range:
#     number += 1
#     print(number)

# Ввести с клавиатуры строку.
# Вывести эту же строку вертикально: по одному символу на строку консоли.

# strok = input('Введите текст = ')
# for letter in strok:
#     print(letter)

# Создать список из словарей с оценками учеников разных классов
# школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# Посчитать и вывести средний балл по всей школе.
# Посчитать и вывести средний балл по каждому классу.

score_school = [
    {'school_class': '4', 'scores': [3,4,1,2,5,4]},
    {'school_class': '5', 'scores': [3,5,5,2,5,4]},
    {'school_class': '9', 'scores': [2,2,1,2,5,4]}
]


def middle_score(score_school):
    value = 0
    counter = 0
    for key in score_school:
        score = key.get("scores")
        for x in score:
            counter += 1
        for item in score:
            value = value + item
    print(int(value/counter))

middle_score(score_school)


def class_score(score_school):
