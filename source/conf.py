# -*- coding: utf-8 -*-

"""
Конфигурационный файл для процесса генерации документации с помощью Sphinx

Официальная документация:
    https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

# ######################################################################################################################
# Импорт необходимых инструментов
# ######################################################################################################################


# ######################################################################################################################
# Информация о проекте (Project information)
# ######################################################################################################################

# Название задокументированного проекта
project = 'Sphinx_rtd'

# Автор(ы) проекта
author = 'Dmitry Ryumin (Дмитрий Рюмин)'

# Авторские права
copyright = '2022, Dmitry Ryumin (Дмитрий Рюмин)'

# Версия проекта
version = '0.1'
release = version

# ######################################################################################################################
# Основные настройки (General configuration)
# ######################################################################################################################

# Расширения: https://www.sphinx-doc.org/en/master/usage/extensions
extensions = [
    'sphinx.ext.mathjax', # Отображение формул (JavaScript)
]

# Локализация (язык): https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language
language = 'ru'

# Директории и файлы, которые следуют исключить при сборке
exclude_patterns = []

# ######################################################################################################################
# Настройки для генерации документации в формат HTML (Options for HTML output)
# ######################################################################################################################

# HTML-тема документации: https://sphinx-themes.org/
#     pydata_sphinx_theme
#     sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'

# Путь к пользовательским статическим файлам (изображения, стили (*.css) и тд.)
html_static_path = ['_static']

# Favicon документации
html_favicon = '_static/favicon.ico'

# Отображение надписи "Собрано при помощи Sphinx ..."
html_show_sphinx = True

# Отображение авторских прав
html_show_copyright = True

# ######################################################################################################################
# Настройки для генерации документации в формат LaTeX->PDF (Options for LaTeX output)
# ######################################################################################################################

latex_elements = {
    'preamble': '\\usepackage[utf8]{inputenc}',
    'babel': '\\usepackage[russian]{babel}',
    'cmappkg': '\\usepackage{cmap}',
    'fontenc': '\\usepackage[T1,T2A]{fontenc}',
    'utf8extra':'\\DeclareUnicodeCharacter{00A0}{\\nobreakspace}',
}

latex_documents = [
  ('index', 'PDF.tex', u'PDF', u'Dmitry Ryumin', 'manual'),
]