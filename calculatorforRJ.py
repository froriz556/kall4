print("Введите 1-ое число:")
a = int(input())
print("Введите 2-ое число:")
b = int(input())
message = '''
Выберете математическую операцию:

+ : Сложение
- : Вычитание
/ : Деление
* : Умножение

Ваш выбор:
'''
operation = input(message)
if operation == '+':
    print('Сложение')
    d = a + b
elif operation == '-':
    print('Вычитание')
    d = a - b
elif operation == '/':
    print('Деление')
    d = a / b
elif operation == '*':
    print('Умножение')
    d = a * b
else:
    print('Неизвестная операция')
print("Результат:", d)