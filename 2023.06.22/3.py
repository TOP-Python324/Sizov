from pathlib import Path
from utils import load_file

def ask_for_file() -> str:
    """ запрашивает у пользователя путь к потерянному файлу и копирует этот файл с помощью функции load_file"""
    
    while True:
        file_path = input('введите путь к файлу: ')
        file_path = Path(file_path)

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
# >>>    