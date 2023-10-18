'''1. Создать родительский класс auto, у которого есть атрибуты: brand, age, color, mark и weight.
 А так же методы: move, birthday и stop. Методы move и stop выводят сообщение на экран «move» и «stop»,
  a birthday увеличивает атрибут аде на 1. Атрибуты brand, age и mark являются обязательными при объявлении объекта.'''

import time

class Auto:
    def __init__(self, brand, age, mark, color='', weight=''):
        self.brand = brand
        self.age = age  # Атрибут
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print('move')  # метод

    def stop(self):
        print('stop')

    def birthday(self):
        self.age += 1
        print(self.age)


car = Auto(brand='Ford', age=25, mark='Mustang')  # экземпляр
print(car.brand)
print(car.age)
print(car.mark)

car.move()
car.stop()
car.birthday()

print('//////////////////////////////')
'''
2. Создать 2 класса truck и car, которые являются наследниками класса auto. Класс truck имеет дополнительный
обязательный атрибут max_load. Переопределённый метод move, перед появлением надписи «move»
выводит надпись «attention», его реализацию сделать при помощи оператора super.
А так же дополнительный метод load. При его вызове происходит пауза 1 сек., затем выдаётся сообщение «load»
и снова пауза 1 сек. Класс car имеет дополнительный обязательный атрибут max_speed и при вызове метода move, после появления надписи «move» должна появиться надпись «max speed is <max_speed>». Создать по 2 объекта для каждого
из классов truck и car, проверить все их методы и атрибуты.'''


class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color='red', weight='123142124'):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print('attention')
        super().move()

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color='', weight=''):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f'max_speed is {self.max_speed}')


a = Truck(brand='Audi', age=12, mark='a1', max_load=123)
b = Truck(brand='Audi', age=12, mark='a1', max_load=1234124152353)
print(a.max_load)
print(b.max_load)

a.move()
a.load()

c = Car(brand='Audi', age=12, mark='a1', max_speed=65)
d = Car(brand='Audi', age=12, mark='a1', max_speed=123213141515124)

c.move()

# '''
# 3. *Для рассмотренного на уроке класса Circle реализовать метод производящий вычитание двух окружностей,
# вычитание радиусов произвести по модулю. Если вычитаются две окружности с одинаковым значением радиуса,
# то результатом вычитания будет точка класса Point.'''
#
# class Point:
#     @staticmethod
#     def point():
#         return '.'
#
#
# class Circle:
#     def __init__(self, r):
#         self.r = r
#
#     def get_circle_area(self):
#         return 3.14 * self.r ** 2
#
#     def __sub__(self, other):
#         # if isinstance(other, Circle):
#             radius_subtraction = abs(self.r - other.r)
#             if radius_subtraction == 0:
#                 return Point.point()
#             else:
#                 return radius_subtraction
#
#
# circle1 = Circle(8)
# circle2 = Circle(-124)
#
# result = circle1 - circle2
#
# print(result)
