""""У цьому коді ми створюємо клас Robot."""""
class Robot:
    """"def __init__(self, name): - оголошення конструктора класу Robot. 
    Конструктор приймає аргумент name"""""

    def __init__(self, name: str) -> None:
        """"self.name = name - ініціалізація властивості name об'єкта Robot значенням, переданим у конструктор."""""
        self.name = name

        """"self.partner = None - ініціалізація властивості partner об'єкта Robot значенням None."""""
        self.partner = None


""""def pair_robots(names): - оголошення функції pair_robots, яка приймає аргумент names"""
def pair_robots(robots: list) -> tuple:
    """"if len(names) != 2: - перевірка, чи має список names довжину не більше 2."""""
    if len(robots) != 2:
        """"raise ValueError("pair_robots очікує список із двох імен") - піднімання винятку ValueError, 
        якщо довжина списку names не дорівнює 2, і виведення повідомлення про помилку."""
        raise ValueError("Function requires a list of exactly two names.")

    """"robot1 = Robot(names[0]) - створення екземпляра класу Robot з іменем, переданим у функцію."""
    """"robot2 = Robot(names[1]) - створення екземпляра класу Robot з іменем, переданим у функцію."""
    robot1 = Robot(robots[0])
    robot2 = Robot(robots[1])

    """"robot1.partner = robot2 - присвоєння значення властивості partner об'єкта robot1 значення об'єкта robot2."""
    """"robot2.partner = robot1 - присвоєння значення властивості partner об'єкта robot2 значення об'єкта robot1."""
    robot1.partner = robot2
    robot2.partner = robot1

    """"return robot1, robot2 - повернення кортежу з об'єктів robot1 і robot2."""
    return robot1, robot2


if __name__ == '__main__':
    """"У цьому коді створюється список роботів, потім викликається функція `pair_robots`, 
    яка створює пари роботів і встановлює їх як партнерів один одному. 
    Потім проводяться перевірки, чи всі умови виконані, і результати виводяться на екран."""

    # Приклад використання
    robots = [
        'Alex',
        'Tom'
    ]

    new_robots = pair_robots(robots)

    print(new_robots[0].name == 'Alex')  # True \
    print(all([isinstance(robot, Robot) for robot in new_robots]))  # True \
    print(new_robots[0].partner is new_robots[1])  # True \
    print(new_robots[1].partner is new_robots[0])  # True
