"""Модуль проверки расстановок на шахматной доске

Ферзь бьет фигуру, если она находиться на одной с ним вертикали, горизонтали или диагонали
Ситуацию указания двух ферзей на одной клетке не обрабатываем
"""
import random as rnd

__all__ = ['check_queen_8x8', 'gen_positions']

_QUEEN_COUNT: int = 8  # максимальное кол-во ферзей
_SIZE_BOARD: int = 8  # размер доски


def check_queen_8x8(positions: list[tuple]) -> bool:
    """Проверка задачи о ферзях.

    :positions: позиции ферзей - кортежи (строка, столбец)
    """
    result = True

    if len(positions) != _QUEEN_COUNT:
        result = False
    else:
        for i in range(_QUEEN_COUNT - 1):  # берем ферзей по списку, исключая последнего (сам себя бить не может)
            if not result:
                break
            row_1, col_1 = positions[i]
            for j in range(i + 1, _QUEEN_COUNT):  # проверяем со следующими до конца списка
                row_2, col_2 = positions[j]
                # Ферзи на одной линии, если координаты строки или столбца у них равны.
                # Ферзи на одной диагонали, если позицию второго можно получить из позиции первого смещением на равное
                # количество строк и столбцов в любую из сторон
                if row_1 == row_2 or col_1 == col_2 or abs(row_1 - row_2) == abs(col_1 - col_2):
                    result = False
                    break

    return result


def gen_positions() -> list[tuple[int, int]]:
    """Генератор позиций ферзей. Генерирует _QUEEN_COUNT позиций, по одному ферзю на строку.
    Для доски размером _SIZE_BOARD
    """
    result = []
    for i in range(_SIZE_BOARD):
        result.append((i, rnd.randint(0, _SIZE_BOARD - 1)))
    return result
