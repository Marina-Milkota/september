#ДЗ на вторник:
#Калькулятор с помощью пользовательских функций
# Функции: сложение, вычитание, умножение, деление (обработать исключение деления на ноль)
# Пятая операция тоже через функцию (для выхода из калькулятора)
# По желанию использовать декоратор

def summ(a,b):print(f"Сумма чисел равна {round(a+b,1)}")
def diff(a,b):print(f"Разность чисел равна {round(a-b,1)}")
def mult(a,b):print(f"Произведение чисел равно {round(a*b,1)}")
def div(a,b):
    try:
        print(f"Деление чисел равно {round(a/b,1)}")
    except ZeroDivisionError:print('На ноль делить нельзя!')

while True:
    operation=input('Выберите операцию:+,-,*,/ (для выхода введите n) ')
    if operation=='n':break
    elif operation=='':
        continue
    elif operation not in '+-*/':
        print('Такого знака нет.Введите операцию корректно!')
        continue
    try:
        number_1 = float(input('Введите первое число: '))
        number_2 = float(input('Введите второе число: '))
    except ValueError:print('Введите число!')
    if operation == '+': summ(number_1,number_2)
    elif operation == '-': diff(number_1,number_2)
    elif operation == '*':mult(number_1,number_2)
    elif operation == '/':div(number_1,number_2)

