user_age = int(input("Введите ваш возраст - "))

def future(user_age):
    if user_age <= 6:
        print("Вам в детский сад")
    elif user_age <= 17:
        print("Вам в школу")
    elif user_age <= 25:
        print("Вам в ВУЗ")
    elif user_age > 26:
        print("Вам на работу")
    else:
        print("Вам куда-то еще")

future(user_age)



def strouk(one, two):
    print(type(one))
    if type(one) and type(two) != str:
        print(0)
    elif one == two:
        print(1)
    elif one != two and len(one) > len(two):
        print(2)
    elif one != two and two == 'learn':
        print(3)
    else:
        print('Что-то пошло не так')

strouk("laa", "learn")

#Test
