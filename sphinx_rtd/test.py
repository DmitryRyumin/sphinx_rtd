# -*- coding: utf-8 -*-

"""
Пример
"""

def sample_function_google(el1: int, el2: int) -> bool:
    """Сумма двух значений

    Args:
        el1 (int): Значение 1
        el2 (int): Значение 2

    Returns:
        bool: Сумма двух значений

    Examples:
        >>> sample_function_google(1, 2)
        3

    .. code-block:: python

        # Сумма двух значений
        sample_function_google(1, 2) # => 3

    Note:
        Текст примечания ...

    See Also:
        Смотреть :ref:`rst-include`

    Raises:
        ConnectionError: If no available port is found.
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
