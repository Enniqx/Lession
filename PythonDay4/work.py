# def hello_user():
#     greeting = ''
#     while greeting != "Хорошо":
#         greeting = input("Как дела? ")
#     else:
#         print('Хорошо, что хорошо!')
#
# hello_user()


# question_answer = {
#                     "Как дела?": "Хорошо",
#                     "Что делаешь?": "Программирую"
#                   }
#
#
# def ask_user(question_answer):
#     while True:
#         answer = ''
#         text = input("Спроси меня о чем-нибудь ")
#         try:
#             print(question_answer[text])
#         except KeyError:
#             if text == 'Help':
#                 get_help()
#             else:
#                 print("Я не знаю такого вопроса. Напиши 'Help', чтобы узнать, что я умею")
#
#
# ask_user(question_answer)
