from shutil import get_terminal_size 
from pathlib import Path
from sys import path
from shutil import copy2
from types import ModuleType


def important_message(text: str) -> str:
    """Генерирует строку, в которой переданный текст будет обрамлён рамкой из символов '=' и '#'."""
    # ИСПРАВИТЬ: согласно условию задачи между боковыми границами рамки и текстом должен быть минимальный отступ два пробела (см. тест в 2.py)
    width = get_terminal_size().columns - 3
    # ИСПРАВИТЬ везде: круглые скобки используются для литерала кортежа, изменения порядка вычисления выражений, вызова функций и записи составного выражения на нескольких строчках — больше нигде и никак
    out = f'#{"="*(width)}#\n#{" "*(width)}#\n'

    # КОММЕНТАРИЙ: очень хорошо, что решили предварительно вычислять длины, а не выполнять конкатенацию строк
    multiline, line_len, i = [[]], 0, 0
    for word in text.split():
        word_len = len(word)
        if line_len + word_len + len(multiline[i]) <= width:
            multiline[i] += [word]
            line_len += word_len
        else:
            multiline += [[word]]
            line_len = word_len
            i += 1

    for line in multiline:
        out += f'#{" ".join(line).center(width)}#\n'

    # ИСПРАВИТЬ везде: круглые скобки используются для литерала кортежа, изменения порядка вычисления выражений, вызова функций и записи составного выражения на нескольких строчках — больше нигде и никак
    out += f'#{" "*(width)}#\n#{"="*(width)}#'
    return out


def load_file(file_path: Path) -> ModuleType:
    """Осуществляет копирование файла по переданному пути в основной каталог."""
    script_dir = Path(path[0])
    copy2(file_path, script_dir)
    # file_name = file_path.stem
    # print(f'{file_name = }')
    import conf as module_object
    return module_object

