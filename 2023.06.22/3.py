from pathlib import Path
from types import ModuleType

# ИСПРАВИТЬ: импорт модулей собственного проекта в общем случае предпочтительнее осуществлять с помощью инструкции import ...
from utils import load_file


# ИСПОЛЬЗОВАТЬ: аннотация объекта модуля может быть осуществлена с помощью строкового литерала или дженерика ModuleType из модуля types стандартной библиотеки
def ask_for_file() -> ModuleType:
    """Запрашивает у пользователя путь к потерянному файлу и копирует этот файл с помощью функции load_file()."""
    while True:
        # ИСПОЛЬЗОВАТЬ: компактную запись там, где это не вредит читаемости кода
        file_path = Path(input('введите путь к файлу: '))
        if file_path.is_file():
            result = load_file(file_path)
            break
        print('! по указанному пути отсутствует необходимый файл !')
    return result


# >>> config_module = ask_for_file()
# введите путь к файлу: E:\!Обучение\top\!Python\Sizov\2023.06.22\conf.py
# ! по указанному пути отсутствует необходимый файл !
# введите путь к файлу: E:\!Обучение\top\!Python\Sizov\2023.06.22\data\conf.py
# >>>
# >>> config_module.defaults
# {'parameter1': 'value1', 'parameter2': 'value2', 'parameter3': 'value3', 'parameter4': 'value4'}


# ИТОГ: отлично — 4/4
