""""Цей рядок оголошує клас Animal. Це базовий клас для всіх тварин."""""
class Animal:
    """Оголошення конструктора класу Animal. Конструктор приймає один аргумент name - ім'я тварини."""""
    def __init__(self, name):

        """Цей рядок присвоює вхідне значення name властивості self.name об'єкта. 
        Таким чином, кожен екземпляр Animal матиме власне ім'я."""""
        self.name = name

    """"Оголошення методу make_sound. Цей метод призначений для перевизначення у похідних класах."""
    def make_sound(self):
        pass


""""Оголошення класу Lion, який наслідується від класу Animal."""
class Lion(Animal):

    """"Оголошення методу make_sound. Цей метод перевизначає метод make_sound у базовому класі Animal."""""
    def make_sound(self):
        return "Roar"


""""Оголошення класу Monkey, який наслідується від класу Animal."""
class Monkey(Animal):

    """"Оголошення методу make_sound. Цей метод перевизначає метод make_sound у базовому класі Animal."""""
    def make_sound(self):
        return "Ooh ooh aah aah"


""""Оголошення класу Snake, який наслідується від класу Animal."""
class Snake(Animal):

    """"Оголошення методу make_sound. Цей метод перевизначає метод make_sound у базовому класі Animal."""""
    def make_sound(self):
        return "Hiss"


""""Оголошення функції create_animals. 
Ця функція створює список тварин і викликає метод make_sound для кожної тварини."""""
def create_animals():
    animals = [
        Lion("Lion"),
        Monkey("Monkey"),
        Snake("Snake")
    ]

    """"Цикл for проходить по списку тварин і викликає метод make_sound для кожної тварини."""""
    for animal in animals:
        print(f"{animal.name} says {animal.make_sound()}")


def main():
    """"Цей рядок викликає функцію create_animals."""""
    create_animals()
