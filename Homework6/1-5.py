# '''1. Декодировать в строку байтовое значение: b'r\xc3\xa9sum\xc3\xa9'. Затем результат преобразовать
# в байтовый вид в кодировке ‘Latin1' и затем результат снова декодировать в строку
# (результаты всех преобразований выводить на экран).'''
# #
# a = b'r\xc3\xa9sum\xc3\xa9'
# b = a.decode('utf-8')
# print(b)
# b = b.encode('Latin1')
# print(b)
# b = b.decode('Latin1')
# print(b)



# '''
# # 2. Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные. Создать файл и записать в него первые 2 строки и
# #  закрыть файл. Затем открыть файл на редактирование и дозаписать оставшиеся 2 строки. В итогом файле должны
# # быть 4 строки, каждая из которых должна начинаться с новой строки.'''
# #
# a = 'Hello Summer'
# b = 'Hello Autumn'
# c = 'Hello Winter'
# g = 'Hello Spring'
#
# with open('seasons.txt', 'w') as writer:
#     writer.write(a + '\n')
#     writer.write(b + '\n')
#
#
# with open('seasons.txt', 'a') as writer:
#     writer.write(c + '\n')
#     writer.write(c + '\n')



# '''
# # 3. Создать словарь в качестве ключа которого будет 6-ти значное число (id), а в качестве значений кортеж состоящий
# # из 2-х элементов – имя(str), возраст(int). Сделать около 5-6 элементов словаря. Записать данный словарь
# # на диск в json-файл.'''
# #
# import json
#
# a = {'754896': ('Kira', 18),
#       '657491': ('lola', 20),
#       '948568': ('Karel', 24),
#       '941274': ('Ivar', 19),
#       '812476': ('Rivalis', 17),
#       '128346': ('Kirill', 18), }
#
# relative_file_path = 'Higher School of Librarians.json'
# file_path = '/home/user/Загрузки/Higher School of Librarians'
#
# with open(file_path, 'w') as f:
#       json.dump(a, f)
#
# with open(relative_file_path, 'w') as f:
#     json.dump(a, f)



# '''
# # 4. Прочитать сохранённый json-файл и записать данные на диск в csv-файл, первой строкой которого озаглавив
# # каждый столбец и добавив новый столбец “телефон”.'''
#
#
#
# import json
# import csv
# my_path_to_json_file_in_back_code = '/home/user/Загрузки/Higher School of Librarians'
#
#
# with open(my_path_to_json_file_in_back_code, 'r') as f:
#     my_json = json.load(f)  # теперь наш файл json это f
# # Мы читаем содержимое файла f и загружаем его в переменную my_json. Теперь my_json содержит данные из JSON-файла.
#
# phone_numbers = ['1241512', '2346385', '9965235', '6892134', '2575383', '2579765']
# # генерируем список номеров
#
# first_line = [['id', 'name', 'age', 'phone']]
# # делаем 1 строку в csv файле
#
# for (id, (name, age)), phone in zip(my_json.items(),phone_numbers):
#     #  мы присваеваем переменным id, (name, age) значения из словаря которого мы распокавали благодаря  data.items():
#     #  id,(name,age) проходятся по значением из словаря , phone проходит по phone_numbers
#     first_line.append([id, name, age, phone])
#
#
# create_csv_file_main = '/home/user/Загрузки/Higher School of Librarians_csv.csv'
# create_csv_file_pycharm = 'Higher School of Librarians_csv.csv'
#
# with open(create_csv_file_main, 'w', newline='', encoding='utf-8') as f:
#     # `newline=''` предотвращает добавление дополнительных пустых строк между строками CSV.
#     csv_writer = csv.writer(f)
#     # теперь csv будет использовать контретно f(наш только что созданный файл) чтобы туда всё записывать!во всех
#      # строчках кода ниже
#     csv_writer.writerows(first_line)  #  записываем `first_line` в CSV
#
# with open(create_csv_file_pycharm, 'w', newline='', encoding='utf-8') as f:
#     csv_writer = csv.writer(f)
#     csv_writer.writerows(first_line)



# '''5. *Прочитать сохранённый csv-файл и сохранить данные в excel-файл,
#  кроме возраста - столбец с этими данными не нужен. '''
#
# import pandas as pd
#
# # Путь к файлу CSV
# csv_file = '/home/user/Загрузки/Higher School of Librarians_csv.csv'
#
# # Чтение CSV-файла и создание DataFrame
# df = pd.read_csv(csv_file, encoding='utf-8')
#
# # Удаление столбца 'age'
# df.drop(columns='age', inplace=True)
#
# # Транспонирование DataFrame и изменение имен столбцов
# df = df.T.rename(columns={i: f'person {i + 1}' for i in range(6)})
# # T: Это превращает строки в столбцы и столбцы в строки,
#
#
#
# # Путь для сохранения Excel-файла
# create_excel_file_main = '/home/user/Загрузки/Higher School of Librarians_excel.xlsx'
# create_excel_file_pycharm = 'Higher School of Librarians_excel.xlsx'
#
# # Сохранение данных в Excel-файлы
# df.to_excel(create_excel_file_main, index=True)
# df.to_excel(create_excel_file_pycharm, index=True)