from shutil import get_terminal_size 
from pathlib import Path
from sys import path
from shutil import copy2

def important_message(text: str) -> str:
    """ Генерирует строку, в которой переданный текст будет обрамлён рамкой из символов '=' и '#'."""
    
    width = get_terminal_size().columns - 3

    out = f'#{"="*(width)}#\n#{" "*(width)}#\n'
    
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

    out += f'#{" "*(width)}#\n#{"="*(width)}#'
    return out
    

def load_file(file_path: Path) -> str:
    """ Осуществляет копирование файла по переданному пути в основной каталог."""    
        
    script_dir = Path(path[0])
    copy2(file_path, script_dir)
    file_name = file_path.stem
#    print(f'{file_name = }')
    import conf as module_object
    return module_object