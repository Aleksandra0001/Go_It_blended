import threading  # Для роботи з потоками.
import time  # Для використання функції sleep.
import random  # Для генерації випадкових чисел.

""""Клас, який представляє годівницю"""
class Feeder:
    """"def __init__(self, radius):: Це конструктор класу Feeder. 
    Він приймає аргумент food і ініціалізує атрибут food та lock об'єкта Feeder."""""

    def __init__(self, food):
        self.food = food  # Кількість їжі у годівниці.
        self.lock = threading.Lock()  # Блокування для синхронізації доступу до годівниці.

    """"def eat(self, animal_name):: Цей метод викликається твариною, яка хоче поїсти.
    Він приймає аргумент animal_name, який використовується для виведення повідомлень.
    Якщо в годівниці є їжа, тоді тварина їсть випадкову кількість їжі (від 1 до 3 одиниць).
    Якщо їжі немає, тоді тварина не може їсти."""

    def eat(self, animal_name):
        with self.lock:  # Використовуємо блокування для синхронізованого доступу до годівниці.
            if self.food > 0:  # Якщо в годівниці є їжа.
                food_eaten = random.randint(1, 3)  # Тварина їсть від 1 до 3 одиниць їжі.
                self.food -= food_eaten  # Зменшуємо кількість їжі у годівниці.
                print(f"{animal_name} їсть. Залишилось їжі: {self.food}")
                if self.food <= 0:  # Якщо їжі немає.
                    print("Годівниця порожня!")
            else:
                print(f"{animal_name} не може їсти. Годівниця порожня!")


""""Клас Animal, який представляє тварину, який наслідує клас Thread."""
class Animal(threading.Thread):
    """"def __init__(self, feeder, name):: Це конструктор класу Animal.
    Він приймає аргументи feeder (годівниця, з якої тварина буде їсти) і name (ім'я тварини)."""""

    def __init__(self, feeder, name):
        super().__init__()  # Викликаємо конструктор батьківського класу.
        self.feeder = feeder  # Годівниця, з якої тварина буде їсти.
        self.name = name  # Ім'я тварини.

    """"def run(self):: Цей метод викликається під час запуску потоку.
    Тут тварина починає їсти і чекає випадковий час перед наступною спробою поїсти."""

    def run(self):
        while self.feeder.food > 0:  # Тварина їсть, поки в годівниці є їжа.
            self.feeder.eat(self.name)  # Тварина їсть.
            time.sleep(random.uniform(0.5, 1.5))  # Тварина чекає випадковий час перед наступною спробою поїсти.


""""Клас, який представляє Зайця, який успадковує клас Animal."""
class Rabbit(Animal):
    """""def __init__(self, feeder):: Це конструктор класу Rabbit,
    який приймає аргумент feeder (годівниця, з якої тварина буде їсти)."""""

    def __init__(self, feeder):
        super().__init__(feeder, 'Заєць')  # Викликаємо конструктор батьківського класу.


"""Клас, який представляє Білку, який успадковує клас Animal."""
class Squirrel(Animal):
    """""def __init__(self, feeder):: Це конструктор класу Squirrel,
    який приймає аргумент feeder (годівниця, з якої тварина буде їсти)."""""
    def __init__(self, feeder):
        super().__init__(feeder, 'Білка')  # Викликаємо конструктор батьківського класу.


"""Клас, який представляє Птаха, який успадковує клас Animal."""
class Bird(Animal):
    """""def __init__(self, feeder):: Це конструктор класу Bird,
    який приймає аргумент feeder (годівниця, з якої тварина буде їсти)."""""
    def __init__(self, feeder):
        super().__init__(feeder, 'Птах')  # Викликаємо конструктор батьківського класу.


def main():
    # Створюємо годівницю з певною кількістю їжі.
    feeder = Feeder(20)

    # Створюємо тварин, які будуть їсти з годівниці та передаємо їм годівницю.
    animals = [Rabbit(feeder), Squirrel(feeder), Bird(feeder)]

    # Запускаємо потоки (тварини починають їсти).
    for animal in animals:
        animal.start()  # start() - запускає потік

    # Чекаємо, поки всі тварини закінчать їсти.
    for animal in animals:
        animal.join()  # join() - чекає завершення потоку

    print("Всі тварини нагодовані.")
