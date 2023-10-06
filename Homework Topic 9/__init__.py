'''
1. Сделать свой класс данных
2. Добавить в класс статикметод
3. Добавить в класс классметод
4. *Создать метакласс
'''

from dataclasses import dataclass


@dataclass
class Genres:
    Fantasy: str = 'Fantasy = 10/10'
    Horror: str = 'Horror = 9/10'
    Detective: str = 'Detective = 5/10'

    @staticmethod
    def Horror_sound():
        print('Booooooo!')

    @classmethod
    def List_genres(cls):
        print(f'Grate_genres =\n{cls.Fantasy}\n{cls.Horror}\n{cls.Detective}')


genres = Genres()
genres.Horror_sound()
genres.List_genres()
print(' атрибуты заменяем по порядку на новые атрибуты ')


class Metaclass(type):
    def __init__(cls, name, bases, attrs):
        cls.one = 'Fantasy = 11/10'
        cls.two = 'Horror = 10/10'
        cls.three = 'Detective = 7/10'
        cls.four_add_new = 'Добавляем атрибут для класса Bot_genres'
        super().__init__(name, bases, attrs)


Bot_genres = Metaclass('Bot_genres', (Genres,), {})
# 0.Bot_genres присваеваем переменной класс 'Bot_genres'
# 1. вызываем метакласс MetaClass
# 2. создаём новый класс Bot_genres
# 3. Bot_genres будет наследовать от класса Genres.
# 4. {} - это словарь атрибутов и методов, которые вы можете определить для Bot_genres
#

bot = Bot_genres()

bot.List_genres()
print(bot.four_add_new)
