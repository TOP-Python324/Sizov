from urllib.request import urlopen
from pathlib import Path
from re import findall, S
from os import path
from json import dump

def json_from_html(url: str, pattern: str, codepage: str = 'utf-8') -> Path:
    """По заданному шаблону извлекает из HTML документа структурируемые данные и помещает их в JSON файл."""
    
    with urlopen(url) as response:
        html_page = response.read()
        
    html_page = html_page.decode(codepage)  

    data = findall(pattern, html_page, S)

    print(data)
    
    
    if url[-5:] == '.html':
        url = url[:-5] .split('/')
        name_file = url[len(url)-1] + '.json'
    else:
        name_file = Path(__loader__.path)
        name_file = path.basename(name_file)
        name_file = name_file.replace('py','json')
    
    #Открываем файл для записи    
    with open(name_file, 'w', encoding='utf8') as json_file: 
        dump(data, json_file, ensure_ascii=False, indent=2) 
    
    return Path(name_file)