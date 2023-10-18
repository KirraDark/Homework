while True:
    a = input('NAME:')
    b = input('AGE:')
    if not b.isdigit() or int(b) <= 0:
        print('Ошибка, повторите ввод')
    elif int(b) > 0 and int(b) < 10:
        print('Привет, шкет', a)
    elif int(b) > 10 and int(b) <= 18:
        print('Как жизнь', a, '?')
    elif int(b) > 18 and int(b) <= 100:
        print('Что желаете', a, '?')
    else:
        print(a, ',', 'вы лжете - в наше время столько не живут...')
        # можно было написать поменьше кода...