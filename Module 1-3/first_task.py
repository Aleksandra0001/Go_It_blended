"""" from abc import ABC, abstractmethod: Цей рядок імпортує два інструменти з модуля abc (абстрактні класи): 
ABC і abstractmethod. ABC - це базовий клас для створення абстрактних класів, і abstractmethod - це декоратор, 
який використовується для визначення абстрактних методів."""""

from abc import ABC, abstractmethod
import math

"""" class Shape(ABC): Тут ми створюємо абстрактний клас Shape, який успадковує клас ABC. 
Це означає, що Shape є абстрактним класом, і ми можемо визначити в ньому абстрактні методи."""


class Shape(ABC):
    """"@abstractmethod: Це декоратор, який вказує, що метод area є абстрактним методом. 
    Абстрактний метод - це метод, який має бути перевизначений у всіх підкласах, які успадковують Shape. 
    У цьому випадку, абстрактний метод area повинен бути реалізований у підкласах Circle і Rectangle."""""

    @abstractmethod
    def area(self):
        pass


""""class Circle(Shape): Тут ми створюємо підклас Circle, 
який успадковує абстрактний клас Shape. 
Цей клас представляє коло."""


class Circle(Shape):
    """"def __init__(self, radius):: Це конструктор класу Circle. 
    Він приймає аргумент radius і ініціалізує атрибут radius об'єкта Circle з переданим значенням радіуса."""""

    def __init__(self, radius):
        self.radius = radius

    """"def area(self):: Цей метод обчислює площу кола, 
    використовуючи формулу π * r^2, де r - це радіус кола."""""

    def area(self):
        return math.pi * self.radius ** 2


""""class Rectangle(Shape):: Тут ми створюємо підклас Rectangle, який також успадковує абстрактний клас Shape. 
Цей клас представляє прямокутник."""""


class Rectangle(Shape):
    """"def __init__(self, width, height):: Це конструктор класу Rectangle. 
    Він приймає аргументи width (ширина) і height (висота) 
    і ініціалізує атрибути width і height об'єкта Rectangle."""""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    """"def area(self):: Цей метод обчислює площу прямокутника, 
    використовуючи формулу ширина * висота."""

    def area(self):
        return self.width * self.height


"""circle = Circle(5): Тут ми створюємо екземпляр класу Circle з радіусом 5.
rectangle = Rectangle(4, 6): Тут ми створюємо екземпляр класу Rectangle з шириною 4 і висотою 6."""

circle = Circle(5)
rectangle = Rectangle(4, 6)

def main():
    """"Перша стрічка виводить площу кола, обчислену за допомогою методу area класу Circle.
Друга стрічка виводить площу прямокутника, обчислену за допомогою методу area класу Rectangle."""""

    print(f'Площа кола: {circle.area()}')
    print(f'Площа прямокутника: {rectangle.area()}')
