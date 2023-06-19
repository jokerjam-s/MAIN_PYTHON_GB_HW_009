# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декораторы

import random as rnd
import csv
from typing import Callable, Tuple

MIN_NUMBER_ON_ROW = 3  # кол-во чисел в строке (минимум)
CSV_FILE = "numbers.csv"
JSON_FILE = "result.json"

# ограничение строк в csv-файла
_MIN_COUNT_ROW = 100
_MAX_COUNT_ROW = 1000

# диапазон генерируемых чисел
_MIN_NUMBER = 0
_MAX_NUMBER = 100


def result_to_json(func: Callable):
    """Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл."""

    import json
    def wrapper(*args, **kwargs):
        # Двойной список solves для решения Python TypeError: ‘float’ object is not subscriptable.
        # https://blog.finxter.com/solved-python-typeerror-float-object-is-not-subscriptable/
        solves = [func(*args, **kwargs)]
        json_res = [dict(a=s[0], b=s[1], c=s[2], x1=s[3], x2=s[4]) for s in solves[0]]
        with open(JSON_FILE, "w", encoding='UTF-8') as file:
            json.dump(json_res, file, indent=2)
        return solves

    return wrapper


def find_root_deco(func: Callable):
    """Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла."""

    def wrapper(*args, **kwargs):
        roots = []
        with open(CSV_FILE, "r", encoding="UTF-8") as file:
            csv_reader = csv.reader(file, dialect="excel", quoting=csv.QUOTE_NONNUMERIC)
            for row in csv_reader:
                x1, x2 = func(row[0], row[1], row[2])
                roots.append([row[0], row[1], row[2], x1, x2])
        return roots

    return wrapper


@result_to_json
@find_root_deco
def find_root(a: int, b: int, c: int):
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
    random_csv(CSV_FILE)
    fun = find_root()
    print(fun)
