# Module 1-2

# Завдання №1

### Створіть абстрактний клас Shape, який буде представляти геометричну фігуру.
### В цьому класі створіть абстрактний метод area(), який буде повертати площу фігури. 
### Створіть два підкласи цього абстрактного класу: Circle і Rectangle. 
### У кожному з цих підкласів реалізуйте метод area() для обчислення площі фігури.
### Потім створіть екземпляри обох підкласів, обчисліть їх площу та виведіть результат.


# Завдання №2

### Створи клас Robot, метод __init__ якого приймає тільки name та записує його у властивість self.name, 
### a властивість self.partner спочатку None.
### Створи функцію pair_robots, яка приймає список з двох імен, створює для кожного екземпляр класу Robot та додає 
### до кожного властивість partner з посиланням на партнера (інший об'єкт). Функція повертає кортеж з роботами.

# Приклад використання

### robots = [ \
###  'Alex', \
###  'Tom' \
### ]

### new_robots = pair_robots(robots)

### new_robots[0].name == 'Alex' # True \
### all([isinstance(robot, Robot) for robot in new_robots]) # True \
### new_robots[0].partner is new_robots[1] # True \
### new_robots[1].partner is new_robots[0] # True


# Завдання №3

### Напиши клас Matrix, який приймає двомірний масив matrix розміром N x N. 
### Метод __init__ повинен зберігати цей масив у властивості self.matrix.

### Клас Matrix повинен мати чотири методи:

### 1. get_diagonal(): повертає діагональ матриці у вигляді списку
### 2. get_counter_diagonal(): повертає зворотню діагональ матриці у вигляді списку
### 3. rotate_rows(number): обертає рядки матриці number разів.
### 4. rotate_columns(number): обертає стовпці матриці number разів.
### Зверніть увагу: потрібно змінити атрибут self.matrix у методах rotate_rows та rotate_columns.

# Приклад використання
###    matrix_inst = Matrix([
###        [1, 2, 3],
###        [4, 5, 6],
###        [7, 8, 9]
###    ])

### print(matrix_inst.get_diagonal())  # [1, 5, 9]
### print(matrix_inst.get_counter_diagonal())  # [3, 5, 7]

### matrix_inst.rotate_rows(1)
### matrix_inst.rotate_columns(1)