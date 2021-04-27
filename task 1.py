"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
| 31 22 |
| 37 43 |
| 51 86 |

| 3 5 32 |
| 2 4 6 |
| -1 64 -8 |

| 3 5 8 3 |
| 8 3 7 1 |
"""
import random
import itertools


class Matrix:
    def __init__(self, values):
        self.values = values

    def __str__(self):
        matrix = ''
        for lines in self.values:
            matrix += f'{lines}\n'
        return matrix.replace('[', '').replace(',', '').replace(']', '').replace(' ', '\t')

    def __add__(self, other):
        sum_matrix = []
        result_matrix = []
        line = []

        def line_generator(length):
            empty_line = [0 for i in range(length)]
            return empty_line

        temp_matrix = list(itertools.zip_longest(self.values, other.values, fillvalue=line_generator(
            max(len(self.values[0]), len(other.values[0])))))

        for i in temp_matrix:
            temp_line = list(itertools.zip_longest(*i, fillvalue=0))
            sum_matrix.append(temp_line)

        for l in sum_matrix:
            for i in l:
                line.append(sum(i))
            result_matrix.append(line)
            line = []
        return Matrix(result_matrix)


def random_matrix(lines, columns):
    matrix = []
    for i in range(lines):
        matrix.append([random.randint(0, 9) for n in range(columns)])
    return matrix


matrix_01 = Matrix(random_matrix(7, 2))
matrix_02 = Matrix(random_matrix(5, 5))
print('********************* Первая матрица ***************************')
print(matrix_01)
print('********************* Вторая матрица ***************************')
print(matrix_02)
print('********************* Сумма матриц ***************************\n')
print(matrix_01.__add__(matrix_02))