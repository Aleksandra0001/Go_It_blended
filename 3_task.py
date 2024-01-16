""""class Matrix:: Визначення класу з ім'ям Matrix"""""


class Matrix:
    """"def __init__(self, matrix):: Визначення конструктора класу Matrix, який приймає один аргумент matrix"""""

    def __init__(self, matrix):

        """"self.matrix = matrix - ініціалізація властивості matrix об'єкта 
        Matrix значенням, переданим у конструктор."""""
        self.matrix = matrix

    """"def get_diagonal(self):: Визначення методу get_diagonal, який не приймає аргументів."""""

    def get_diagonal(self):

        """"return [self.matrix[i][i] for i in range(len(self.matrix))]: Метод повертає список, 
        який містить значення елементів головної діагоналі матриці. 
        Він використовує списковий вираз та цикл для створення цього списку."""""
        return [self.matrix[i][i] for i in range(len(self.matrix))]

    """def get_counter_diagonal(self):: Визначення методу get_counter_diagonal, аналогічного до попереднього, 
але цей метод повертає список значень зворотної діагоналі матриці."""""

    def get_counter_diagonal(self):
        return [self.matrix[i][len(self.matrix) - 1 - i] for i in range(len(self.matrix))]

    """def rotate_rows(self, number):: Визначення методу rotate_rows, який приймає аргумент number - 
    кількість разів для обертання рядків матриці."""

    def rotate_rows(self, number):

        """"Цикл, який виконується number % len(self.matrix) разів. 
        % - це операція отримання залишку від ділення."""""
        for _ in range(number % len(self.matrix)):
            """"Цикл, який виконується для кожного рядка матриці.
            Виконує метод insert для кожного рядка матриці,
            який вставляє останній елемент рядка на початок рядка."""""
            self.matrix.insert(0, self.matrix.pop())

    """Визначення методу rotate_columns, аналогічного до rotate_rows, 
    але цей метод обертає стовпці матриці."""""
    def rotate_columns(self, number):
        """"Цикл, який виконується number % len(self.matrix) разів, 
        так само як у методі rotate_rows"""""
        for _ in range(number % len(self.matrix)):
            """"Цикл, який виконується для кожного рядка матриці."""""
            for i in range(len(self.matrix)):
                """"Виконує метод insert для кожного рядка матриці,
                який вставляє останній елемент рядка на початок рядка."""""
                self.matrix[i].insert(0, self.matrix[i].pop())


if __name__ == '__main__':
    """"В цьому прикладі створюється об'єкт класу Matrix, 
    який представляє двовимірну матрицю чисел. 
    Потім викликаються методи для отримання діагоналей матриці та обертання рядків і стовпців на один раз вправо. 
    Результати виводяться на екран."""

    # Приклад використання
    matrix_inst = Matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    print(matrix_inst.get_diagonal())  # [1, 5, 9]
    print(matrix_inst.get_counter_diagonal())  # [3, 5, 7]

    matrix_inst.rotate_rows(1)
    matrix_inst.rotate_columns(1)
