import threading
import time
import random


class Feeder:
    def __init__(self, food):
        # Ініціалізація годівниці з певною кількістю їжі
        pass

    def eat(self, animal_name):
        # Обробка спроби тварини поїсти
        pass


class Animal(threading.Thread):
    def __init__(self, feeder, name):
        # Ініціалізація тварини з іменем і годівницею
        pass

    def run(self):
        # Логіка виконання потоку для тварини
        pass


class Rabbit(Animal):
    def __init__(self, feeder):
        # Ініціалізація зайця
        pass


class Squirrel(Animal):
    def __init__(self, feeder):
        # Ініціалізація білки
        pass


class Bird(Animal):
    def __init__(self, feeder):
        # Ініціалізація птаха
        pass


def main():
    # Створення годівниці та тварин
    # Запуск потоків для тварин
    # Чекання завершення всіх потоків
    pass


if __name__ == "__main__":
    main()
