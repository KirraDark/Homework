# '''
# Задания для самостоятельной работы
# 1. Сделать калькулятор
# 2. Обернуть его в try/except
# 3. *Сделать свое исключение и подключить к try/except
# '''
# while True:
#     try:
#         a = float(input('Введите число :'))
#         b = input('Введите операцию :')
#         c = float(input('Введите число :'))
#
#         if len(str(a)) > 5 or len(str(b)) > 5:
#             raise ValueError('Лень считать')
#
#         try:
#             if b == '+':
#                 print(a + c)
#             elif b == '-':
#                 print(a - c)
#             elif b == '*':
#                 print(a * c)
#             elif b == '/':
#                 print(a / c)
#             elif b == '//':
#                 print(a // c)
#             else:
#                 print('неправильная операция или такого в калькуляторе нет')
#
#         except ZeroDivisionError:
#             print('Вы дурак')
#
#     except ValueError as value_error:
#         print(f'Ошибка: {value_error}')


'''
1. Создать генератор геометрической прогрессии
2. Подключить дебаггинг
3. *Сделать функцию для фильтрации емейла (регуляркой)
Правила валидации имейлов «username@hostname>>:
-username может в себе содержать:
латиницу цифры
знаки! #
% & ' *+ − / = ? ^
{ | } ~
точку, за исключением первого и последнего знака, которая не может повторятся - hostname cостоит из нескольких
компонентов, разделённых точкой и не превышающих 63 символа. Компоненты, в свою очередь, состоят из латинских букв,
 цифр и дефисов, причём дефисы не могут быть в начале или в конце компонента.'''

# def geometry_progression(a,r,n):
#     for i in range(n):
#         yield a
#         a *= r
#
# a = 2
# r = 3
# n = 10
# geom = geometry_progression(a, r, n)
#
# for c in geom:
#     print(c)

import re


def v_email(email):
    re1 = r'^[a-zA-Z0-9!#%&\'*+\-\/=?^{|}~]+@[a-zA-Z0-9\-]+(\.[a-zA-Z0-9\-]+)+$'
    if re.match(re1, email):  # example123@my-host.com
        part1 = email.split('@')  # example123  и my-host.com
        part2 = part1[1]  # my-host.com
        part3 = part2.split('.')  # my-host и com

        for i in part3:
            if len(i) > 63 or i.startswith('-') or i.endswith('-'):
                return 'Ошибка неправельный ввод'
        else:
            return 'Email корректен'

    else:
        return 'Ошибка неправельный ввод'



email = input()
result = v_email(email)
print(result)