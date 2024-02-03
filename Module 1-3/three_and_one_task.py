class Animal:
    def __init__(self, name, health_status, diet):
        self.name = name
        """"Додаємо властивості health_status і diet."""
        self.health_status = health_status
        self.diet = diet

    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        return "Roar"


class Monkey(Animal):
    def make_sound(self):
        return "Ooh ooh aah aah"


class Snake(Animal):
    def make_sound(self):
        return "Hiss"


""""Клас, що відповідає за догляд за тваринами.
Містить два статичні методи:
check_health(animal) - виводить інформацію про здоров'я заданої тварини.
feed_animal(animal) - виводить інформацію про годування заданої тварини згідно з її дієтою."""


class ZooKeeper:
    @staticmethod
    def check_health(animal):
        print(f"Checking health of {animal.name}. Status: {animal.health_status}")

    @staticmethod
    def feed_animal(animal):
        print(f"Feeding {animal.name} with {animal.diet}")


""""Клас для управління щоденним розкладом тварин.
__init__(animal) - конструктор ініціалізує об'єкт для певної тварини та створює словник (activities) для збереження 
її активностей.
add_activity(time, activity) - метод для додавання нової активності у певний час.
display_schedule() - метод для відображення всього розкладу активностей тварини."""


class ActivitySchedule:
    def __init__(self, animal):
        self.animal = animal
        self.activities = {}

    def add_activity(self, time, activity):
        self.activities[time] = activity

    def display_schedule(self):
        print(f"Schedule for {self.animal.name}:")
        for time, activity in self.activities.items():
            print(f"At {time}, {activity}")


""""Функція створює об'єкти тварин (lion, monkey, snake), ініціалізує ZooKeeper та ActivitySchedule.
Вона використовує методи ZooKeeper для перевірки здоров'я та годування тварин.
Також створює розклад активностей для однієї з тварин (у вашому випадку для monkey, хоча змінна називається 
lion_schedule, це може бути помилка)."""


def create_animals():
    lion = Lion("Lion", "Healthy", "Meat")
    monkey = Monkey("Monkey", "Healthy", "Fruits")
    snake = Snake("Snake", "Healthy", "Mice")

    zookeeper = ZooKeeper()
    zookeeper.check_health(lion)
    zookeeper.feed_animal(lion)

    animal_schedule = ActivitySchedule(lion)
    animal_schedule.add_activity("08:00", "Morning exercise")
    animal_schedule.add_activity("12:00", "Lunch break")
    animal_schedule.add_activity("15:00", "Public show")

    animal_schedule.display_schedule()


def main():
    create_animals()
