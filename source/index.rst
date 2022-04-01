.. meta::
   :description: The reStructuredText plaintext markup language
   :keywords: plaintext, markup language

Welcome to Sphinx_rtd's documentation!
======================================

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Содержание:

   example1
   example2

.. contents:: Содержание файла:
   :depth: 6

Заголовок 1 уровня
==================

Заголовок 2 уровня
------------------

Заголовок 3 уровня
******************

Заголовок 4 уровня
++++++++++++++++++

Заголовок 5 уровня
~~~~~~~~~~~~~~~~~~

Заголовок 6 уровня
""""""""""""""""""

Первый абзац ...

Строки параграфов начинаются от левой границы
и отделяются параграфы друг от друга пустой строкой.

**жирный**

*курсив*

``Текст в рамке``

#. Один
#. Два
#. Три

Или:

13. Тринадцать
14. Четырнадцать
#. Пятьнадцать
#. Шестьнадцать

* Один
* Два
* Три

* Первый уровень
   * Второй уровень
      * Третий уровень

#. Один
   * Маркер
#. Два
   #. Номер
   #. Номер

| H\ :sub:`2`\ O
| E = mc\ :sup:`2`

:Первый: В прямоугольном треугольнике квадрат длины
         гипотенузы равен сумме квадратов длин катетов.

Второй
   В прямоугольном треугольнике квадрат длины
   гипотенузы равен сумме квадратов длин катетов.

Основной текст:
   Цитата неизвестного человека

   -- Аноним

.. epigraph::
   *"Если бы двери восприятия были чисты, всё
   предстало бы человеку таким, как оно есть -- бесконечным"*

   -- Уильям Блэйк

Числовая сноска [5]_.

.. [5] Сюда ведет числовая сноска.

Сноски с автоматической [#]_ нумерацией [#]_.

.. [#] Это первая сноска.
.. [#] Это вторая сноска.

Авто­символ сносок используйте вот так [*]_, [*]_ и [*]_.

.. [*] Это первый символ.
.. [*] Это второй символ.
.. [*] Это третий символ.

Ссылки на цитаты выглядят так [CIT2002]_.

.. [CIT2002] Это цитата (как часто используемая в журналах).

.. Это комментарий
   Многострочный комментарий

Посмотрим на исходный код: ::

   Пример исходного кода

Copyright |copy| 2015, |DR (TM)| |---| все права защищены.

.. |copy| unicode:: 0xA9 .. знак копирайта
.. |DR (TM)| unicode:: Dmitry Ryumin U+2122 .. символ торговой марки
.. |---| unicode:: U+02014 .. длинное тире

.. |date| date:: %d.%m.%Y
.. |time| date:: %H:%M

Текущая дата |date| и время |time|

----

.. include:: include.rst

----

1. Внешние ссылки выглядят так: ссылка_.

.. _ссылка: http://librerussia.blogspot.ru/

2. Если несколько слов, тогда так: `ссылка в несколько слов`_.

.. _`ссылка в несколько слов`: http://librerussia.blogspot.ru/

3. `Более компактная запись ссылок <http://librerussia.blogspot.ru/>`_

Внутренние ссылки делаются так_

.. _так:

Ссылка на раздел создается так `Ссылка на заголовок`_ .
Достаточно в обратных кавычках написать название заголовка.

Ссылка на заголовок
===================

Вставка изображения между слов |favicon| осуществляться с помощью функции автозамены:

.. |favicon| image:: _static/favicon.ico
   :scale: 20 %

.. figure:: _static/sphinx.jpg
   :scale: 20 %
   :align: center
   :alt: Альтернативный текст

   Подпись изображения

   Легенда изображения.

.. table:: Заголовок таблицы (Внимание! Отступ таблицы относительно команды .. table:: обязателен)

   +------------------------+------------+----------+----------+
   | Header row, column 1   | Header 2   | Header 3 | Header 4 |
   | (header rows optional) |            |          |          |
   +========================+============+==========+==========+
   | body row 1, column 1   | column 2   | column 3 | column 4 |
   +------------------------+------------+----------+----------+
   | body row 2             | Cells may span columns.          |
   +------------------------+------------+---------------------+
   | body row 3             | Cells may  | - Table cells       |
   +------------------------+ span rows. | - contain           |
   | body row 4             |            | - body elements.    |
   +------------------------+------------+---------------------+

.. table:: Простая таблица
   :align: center

   =====  =====  =======
   A      B      A and B
   =====  =====  =======
   False  False  False
   True   False  False
   False  True   False
   True   True   True
   =====  =====  =======

.. table:: Простая таблица со сложной шапкой

   =====  =====  ======
      Inputs     Output
   ------------  ------
   A      B      A or B
   =====  =====  ======
   False  False  False
   True   False  True
   False  True   True
   True   True   True
   =====  =====  ======

.. csv-table:: CSV-таблица
   :header: "Treat", "Quantity", "Description"
   :widths: 15, 10, 30

   "Albatross", 2.99, "On a stick!"
   "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
   crunchy, now would it?"
   "Gannet Ripple", 1.99, "On a stick!"

.. list-table:: Таблица в виде списка
   :widths: 15 10 30
   :header-rows: 1

   * - Treat
     - Quantity
     - Description
   * - Albatross
     - 2.99
     - On a stick!
   * - Crunchy Frog
     - 1.49
     - If we took the bones out, it wouldn't be
       crunchy, now would it?
   * - Gannet Ripple
     - 1.99
     - On a stick!

.. math::

   \alpha_t(i) = P(O_1, O_2, ... O_t, q_t = S_i \lambda)

.. attention:: Блок **Внимание**, команда: ``.. attention::``

.. caution:: Блок **Осторожно**, команда: ``.. caution::``

.. danger:: Блок **Опасно**, команда: ``.. danger::``

.. error:: Блок **Ошибка**, команда: ``.. error::``

.. hint:: Блок **Подсказка**, команда: ``.. hint::``

.. important:: Блок **Важно**, команда: ``.. important::``

.. note:: Блок **Примечание**, команда: ``.. note::``

.. tip:: Блок **Совет**, команда: ``.. tip::``

.. warning:: Блок **Предупреждение**, команда: ``.. warning::``

.. code-block:: python
   :linenos:

   def some_function():
      """
      Функция
      """

      interesting = False

      print('This line is highlighted.')
      print('This one is not...')
      print('...but this one is.')

----

.. literalinclude:: python/main.py
   :language: python
   :emphasize-lines: 13-15,21-23
   :encoding: utf-8
   :lines: 3-25,38-41
   :linenos:

----

Формула в предложении :math:`a^2 + b^2 = c^2`.

.. math:: e^{i\pi} + 1 = 0
   :label: euler

Формула :eq:`euler` представляет собой Тождество Эйлера.

Например, для ссылки на пункт :ref:`table-label2` из
раздела :ref:`rst-include` я использовал следующие команды

Теперь сделаем ссылку на изображение :ref:`my-favicon`:

.. glossary::
   :sorted:

   Трансценденция
      Философский термин, характеризующий то, что
      принципиально недоступно опытному познанию
      или не основано на опыте.

   Бозон
      Частица с целым значением спина.

   А
      Описание А

:abbr:`LIFO (last-in, first-out)`

:menuselection:`Файл --> О&ткрыть`
:guilabel:`&Открыть`

Номер релиза: |release|

Номер версии: |version|

Текущая дата: |today|

.. seealso:: Блок с дополнительной информацией.

.. sidebar:: Боковая врезка
   :subtitle: Optional Sidebar Subtitle

   Subsequent indented lines comprise
   the body of the sidebar, and are
   interpreted as body elements.

.. rubric:: Пример рубрики

Текст рубрики

.. hlist::
   :columns: 3

   * A list of
   * short items
   * that should be
   * displayed
   * horizontally

.. function:: pyfunc(n: int = 1)

   Описание функции Python.

Дополнительная строка 1

Дополнительная строка 2

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
