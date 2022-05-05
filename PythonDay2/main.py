balance = 100
price = 200

print(bool(balance < 0 or price > balance))

if balance < 0 or price > balance:
    print("Пополните баланс!")
else:
    print("Пожалуйста, пополните баланс!")
