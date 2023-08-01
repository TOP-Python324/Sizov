import os
from pathlib import Path

def list_files(path: 'str') -> tuple:
    """Возвращает кортеж с именами файлов в каталоге по переданному пути.
"""
    DIR_PATH = Path(path)
    list_file = os.listdir(DIR_PATH)
    out = []
    for file in list_file:
        local_path = DIR_PATH / file
        if local_path.is_file():
            out.append(file)
    #return tuple(os.listdir(DIR_PATH))
    return tuple(out)
    
# D:\TOP\Sizov>python -i 2023.06.22\1.py
# >>> list_files(r'2023.06.22/data')
# ('7MD9i.chm', 'conf.py', 'E3ln1.txt', 'F1jws.jpg', 'le1UO.txt', 'q40Kv.docx', 'questions.quiz', 'r62Bf.txt', 'vars.py', 'xcD1a.zip')
# >>>