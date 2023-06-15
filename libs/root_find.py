# Нахождение корней квадратного уравнения <br>
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.<br>

__all__ = ['find_root', 'random_csv']

import random as rnd
import csv

MIN_NUMBER_ON_ROW = 3  # кол-во чисел в строке (минимум)

# ограничение строк в csv-файла
_MIN_COUNT_ROW = 100
_MAX_COUNT_ROW = 1000

# диапазон генерируемых чисел
_MIN_NUMBER = 0
_MAX_NUMBER = 100


def find_root(a: int, b: int, c: int) -> (int, int | None, None):
    """Поиск корней квадратного уравнения"""
    x1 = x2 = None
    d = b * b - 4 * a * c
    if d > 0:
        x1 = (-b + d ** 0.5) / 2 * a
        x2 = (-b - d ** 0.5) / 2 * a
    elif d == 0:
        x1 = x2 = -b / 2 * a
    return x1, x2


def random_csv(file_name: str, /, count_row: int = _MIN_COUNT_ROW, count_number: int = MIN_NUMBER_ON_ROW):
    """Генерация случайных чисел в csv файл"""
    data = []
    if not _MIN_COUNT_ROW <= count_row <= _MAX_COUNT_ROW:
        count_row = MIN_NUMBER_ON_ROW

    if count_number < MIN_NUMBER_ON_ROW:
        count_number = MIN_NUMBER_ON_ROW

    for _ in range(count_row):
        data.append([rnd.randint(_MIN_NUMBER, _MAX_NUMBER) for _ in range(count_number)])

    with open(file_name, "w", encoding="UTF-8", newline='') as file:
        csv_writer = csv.writer(file, dialect="excel", quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writerows(data)


if __name__ == '__main__':
    print(find_root(2, 3, 3))
    print(find_root(2, 7, 3))
    print(find_root(4, 7, 3))

    random_csv("numbers.csv")
