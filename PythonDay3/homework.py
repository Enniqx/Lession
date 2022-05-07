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


# def middle_score(score_school):
#     value = 0
#     counter = 0
#     for key in score_school:
#         score = key.get("scores")
#         for x in score:
#             counter += 1
#         for item in score:
#             value = value + item
#     print(int(value/counter))
#
# middle_score(score_school)


# def class_score(score_school):
#     counter = 0
#     for item in score_school:
#         clas = item.get("school_class")
#         a = clas
#     for scores in score_school:
#         scor = sum(scores.get("scores"))
#         b = scor / 6
#         print(f"В {a} классе средний балл {b}")
#
# class_score(score_school)

school_classes= [
                {'school_class': '4a', 'scores': [3,4,4,5,2]},
                {'school_class': '5b', 'scores': [5,2,3,5,4]},
                {'school_class': '6a', 'scores': [4,5,2,4,3]}
                ]

#Посчитать и вывести средний балл по всей школе.
def average_school (dict_list):
    for item in dict_list:
        class_res=0
        len_avg=0
        class_res=sum(item.get('scores'))+class_res
        len_avg=len(item.get('scores'))+len_avg

    res = class_res/len_avg
    print ('Classes average: '+str(res) )
average_school(school_classes)
#Посчитать и вывести средний балл по каждому классу.
def class_avr(dict_list):
    for item in dict_list:
        school_class= item.get('school_class')
        res =  sum(item.get('scores'))/len(item.get('scores'))
        print ('Class: '+school_class+' average: '+str(res) )
class_avr(school_classes)
