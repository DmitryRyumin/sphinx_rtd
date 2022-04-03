# -*- coding: utf-8 -*-

"""
Пример
"""

def sample_function_google(el1: int, el2: int) -> bool:
    """Сумма двух значений

    Args:
        el1: Значение 1
        el2: Значение 2

    Returns:
        Сумма двух значений

    """

    return el1 + el2

def str_concat(str1: str, str2: str) -> str:
    """Конкатенация двух строк

    Args:
        str1 (str): Строка 1
        str2 (str): Строка 2

    Returns:
        str: Новая строка из двух строк

    """

    return str1 + ' ' + str2

sample_function_google(1, 2)
